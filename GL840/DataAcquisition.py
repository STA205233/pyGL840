"""
data_acquisition
====

This is data acquisition tool for GL840.

How To Use
--

(1) Construct Data_Acquisition object.

    >>> daq = Data_Acquisition(csv_file="test.csv", mongo=True)
(2) If you use MongoDB or csv writer, call initialize_multi or initialize_single method of Data_Acquisition class.

    >>> daq.initialize_multi()
    or
    >>> daq.initialize_single()
(3) Each time you call data_acquire method, data acquisition will be made.

    >>> daq.data_acquire()

Classes
--

GL840_status
    Manage the GL840 status.
GL840_data
    Data structure for GL840.
Data_Acquisition
    Acquire the data of GL840.
Writer
    Write the data into csv file.

Exception
--
NotInitializedMultiException
    Raised when initialize_multi method is not called and DAQ process starts.

Example
--

An example is shown below.

---------------------
Author : Shota Arai
Date : 2022/12/12

"""

import requests
import requests.auth
import re
from typing import Callable, Optional, Any, Union
import csv
import time
from datetime import datetime
from os.path import exists

from multiprocessing import Process, Queue
from .MongoDBHandler import MongoDBPusher, MongoDBData, MongoDBSection
import queue
import os


TI_DIVIDE = 64


class GL840Configuration():
    """
    Manage the GL840 configuration.

    Attributes
    --

    ip : str, default "192.168.0.1"
        IP address of GL840's Web server.
    port : int, default 80
        Port of GL840's Web server.
    username: Optional[str], default None
        User name when the authentication mode in web server is on.
    channels : int, default 20
        The number of channels of GL840. If your GL840 is attached with Extension board, you must change this value.
    channel_name : list of str
        The name of each channel. Default is "Ch i", where i is channel ID.
    """

    def __init__(self, ip: str = "192.168.0.1", port: int = 80, username: Optional[str] = None, password: Optional[str] = None, channels: int = 20) -> None:
        """
        Manage the GL840 status.

        Parameters
        --

        ip : str, default "192.168.0.1"
            IP address of GL840's Web server.
        port : int, default 80
            Port of GL840's Web server.
        username : Optional[str], default 80
            Username when the authentication mode in web server is on.
        password : Optional[str], default None
            password when the authentication mode in web server is on.
        channels : int, default 20
            The number of channels of GL840. If your GL840 is attached with Extension board, you must change this value.

        Return
        --

        None
        """
        self.ip = ip
        self.port = port
        self.__password = password
        self.username = username
        self.channels = channels
        self.__channel_status: list[bool] = [True for i in range(channels)]
        self.__channel_name: list[str] = [f"Ch{i+1}" for i in range(channels)]

    @property
    def password(self) -> Optional[str]:
        return self.__password

    @password.setter
    def password(self, value: Optional[str]) -> None:
        self.__password = value
        print("Password was set.")

    @property
    def channel_status(self) -> list[bool]:
        return self.__channel_status

    @channel_status.setter
    def channel_status(self, value: list[bool]) -> None:
        if len(value) != self.channels:
            raise ChannelNotMatchError(
                f"The length of channel status ({len(value)}) does not match the number of channels ({self.channels})")
        self.__channel_status = value
        for i in range(len(value) - 1, -1, -1):
            if not value[i]:
                del self.__channel_name[i]
        print(
            f"Channel Status Updated!\n Channel Status: {self.__channel_status}\n Channel name: {self.__channel_name}")

    @property
    def channel_name(self) -> list[str]:
        return self.__channel_name

    @channel_name.setter
    def channel_name(self, value: list[str]) -> None:
        if len(value) != len(set(value)):
            raise ChannelNotMatchError(
                f"The length of input array ({len(value)}) is invalid. It must be the same as The number of channels ({self.channels}). Note that each channel name must be different")
        self.__channel_name = value
        print(f"Channel Status Updated!\n Channel Status: {self.__channel_status}\n Channel name: {self.__channel_name}")


class NotInitializedMultiException(Exception):
    pass


class GL840Data(MongoDBData):
    """
    Data structure for GL840.

    Attributes
    --

    data : list[float]
        The measured data in each channel. The length must be the same size as the number of the channels.
    time : datetime
        The time when the constructor is called.
    dict : dict[str, Any]
        The data including time and data. It is used for mongoDB push.

    """

    def __init__(self, data: list[Any], status: GL840Configuration, directory: str = "GL840", document: str = "GL840", section: str = "GL840") -> None:
        """
        Data structure for GL840.

        Parameters
        --

        data: list[float]
            Measured data in each channel.
        status: GL840_status
            Status data of GL840.

        Return
        --
        None
        """

        if len(data) != len(status.channel_name):
            raise ChannelNotMatchError(
                f"Length of data ({len(data)}) does not match channel number ({len(status.channel_name)}).")
        self.data: list[Any] = data
        self.time: datetime = datetime.now()
        self.dict: dict[str, Union[float, None, str, list[Any]]] = {
            "Time": str(self.time), }
        for i in range(len(status.channel_name)):
            self.dict[f"{status.channel_name[i]}"] = self.data[i]
        self.section = MongoDBSection(section, self.dict)
        super().__init__(directory, document, [
            self.section, ])


class DataAcquisition():
    """
    Acquire the data of GL840.

    Attributes
    --

    csv_file : Optional[str]
        Path of csv file written the data into.
    write_interval : int, default 10



    """

    def __init__(self, status: GL840Configuration, write_interval: int = 10, maxsize_query: int = 50, strip_word: str = "<b>&nbsp;</b>", pat: str = r"<b>&nbsp;([\+\-]\s*?[0-9.]+?|[Of]+?|[BURNOT]+?|[\+]+?)</b>", replace_pat_list: dict[str, str] = {r"<font size=6>&nbsp;</font>": ""}, csv_file_base: Optional[str] = None, mongo: Optional[MongoDBPusher] = None, override: bool = False, num_event_per_file: int = 10000) -> None:
        """
        Acquire the data of GL840

        Parameters
        --

        status : GL840_status
            The status instance of GL840.
        write_interval : int, default 10
            Interval between writing the data into csv file.
        maxsize_query : int, default 50
            The size of query between Writer process and DAQ process. If more data than this value is unwritten, incoming data will vanish.

        """
        self.csv_file_base = csv_file_base
        self.write_interval = write_interval
        self.maxsize = maxsize_query
        self.strip_word = strip_word
        self.__initialized = False
        self.__is_single = False
        self.__override = override
        self.config = status
        self.pattern = re.compile(pat)
        self.func: list[Callable] = [
            lambda x: x for i in range(self.config.channels)]
        self.mongo_client = mongo
        self.replace_pat = replace_pat_list
        self.num_event_per_file = num_event_per_file
        self.event_index = 0
        self.file_index = 0
        self.timeout_multi = 0
        if self.csv_file_base is None:
            self.__csv_file = ""
        else:
            self.__csv_file = self.csv_file_base + str(self.file_index) + ".csv"

    def set_function(self, index: int, func: Callable) -> None:
        if index > self.config.channels:
            print(f"Index({index}) is larger than the number of channels({self.config.channels})")
            return
        elif index < 0:
            print(f"Index({index}) is smaller than 0")
        self.func[index] = func

    def initialize_multi(self, timeout: int = 5) -> int:
        """
        Initialize multi process.

        Parameters
        --

        timeout : int, default 5

        """
        if self.__initialized:
            return 0
        if self.csv_file_base is None:
            self.__initialized = True
            return 0
        if self.num_event_per_file is None:
            print("num_event_per_file is unsupported in multi thread mode")
            return -1
        self.timeout_multi = timeout
        self.query: Queue = Queue(maxsize=self.maxsize)
        self.writer = Writer(csv_file=self.__csv_file,
                             buffer_num=self.write_interval, queue=self.query)
        self.process = Process(
            group=None, target=self.writer.get, args=(timeout,),)
        self.process.start()
        self.writer.write([["Time", *self.config.channel_name], ])
        self.__initialized = True
        return 1

    def initialize_single(self) -> int:
        if self.csv_file_base is None:
            self.__initialized = True
            self.__is_single = True
            return 0
        self.writer = Writer(csv_file=self.__csv_file,
                             buffer_num=self.write_interval, override=self.__override)
        self.writer.write([["Time", *self.config.channel_name], ])
        self.__is_single = True
        self.__initialized = True
        return 1

    def data_acquire(self, waitfor: int = 0, timeout: int = 5) -> None:
        if not self.__initialized and self.csv_file_base is not None:
            raise NotInitializedMultiException
        self.__update_file()
        if self.config.username is not None and self.config.password is not None:
            site_data = requests.get(f"http://{self.config.ip}:{self.config.port}/digital.cgi?chgrp=13", auth=requests.auth.HTTPBasicAuth(self.config.username, self.config.password), timeout=timeout)
        else:
            site_data = requests.get(f"http://{self.config.ip}:{self.config.port}/digital.cgi?chgrp=13", timeout=timeout)
        if (site_data.text.find("Unauthorized") >= 0):
            raise requests.ConnectionError("Password authorization failed")
        text = site_data.text
        for _pat in self.replace_pat.keys():
            text = text.replace(_pat, self.replace_pat[_pat])
        data_list: list[Any] = re.findall(self.pattern, text)
        if len(data_list) != self.config.channels:
            raise ChannelNotMatchError(
                f"The length of input data ({len(data_list)}) does not match Channel number ({self.config.channels}).")
        for i in range(self.config.channels - 1, -1, -1):
            if not self.config.channel_status[i]:
                data_list[i] = "Disabled"
                continue
            elif ("Off" in data_list[i] or "BURNOUT" in data_list[i] or "+++++++" in data_list[i]):
                continue
            else:
                data_list[i] = self.func[i](float(data_list[i].replace(" ", "").strip(self.strip_word)))
                data_list[i] = str(data_list[i])
                continue
        self.data = GL840Data(data_list, self.config)
        if self.__initialized:
            if self.__is_single:
                self.writer.write([[self.data.time, *self.data.data], ])
            else:
                self.query.put([self.data.time, *self.data.data])

        if self.mongo_client is not None:
            self.mongo_client.push(self.data)
        del data_list
        time.sleep(waitfor)

    def finalize_multi(self, show_end) -> None:
        if self.__initialized is False:
            return
        self.process.join()
        self.__initialized = False
        if show_end:
            print("Data Acquisition End!")

    def finalize_single(self, show_end: bool) -> None:
        if self.__initialized is False:
            return
        self.__initialized = False
        if show_end:
            print("Data Acquisition End!")

    def __update_file(self) -> None:
        if (self.num_event_per_file is None) or (self.csv_file_base is None):
            return
        if self.event_index >= self.num_event_per_file:
            self.file_index += 1
            self.__csv_file = self.csv_file_base + str(self.file_index) + ".csv"
            if self.__is_single:
                self.finalize_single(False)
                self.initialize_single()
            else:
                self.finalize_multi(False)
                self.initialize_multi(self.timeout_multi)
            self.event_index = 1
        else:
            self.event_index += 1


class ChannelNotMatchError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Writer():
    def __init__(self, csv_file: str, buffer_num: int, queue: Optional[Queue] = None, override: bool = False) -> None:

        self.buffer: list[Any] = []
        self.queue = queue
        self.buffer_num = buffer_num
        self.csv_file = csv_file
        if os.name == "nt":  # If the OS is Windows
            self.__newline: Optional[str] = ""
        else:
            self.__newline = None
        if exists(csv_file) and not override:
            raise FileExistsError(f"{csv_file} does exist!")
        fp = open(self.csv_file, mode="w", newline=self.__newline)
        fp.close()

    def get(self, timeout: int) -> None:
        if self.queue is None:
            print("Writer.get needs self.queue")
            return
        while 1:
            try:
                try:
                    self.buffer.append(self.queue.get(
                        block=True, timeout=timeout))
                except queue.Empty:
                    self.write_buffer()
                    break
                if len(self.buffer) >= self.buffer_num:
                    self.write_buffer()
                else:
                    continue
            except KeyboardInterrupt:
                pass

    def write_buffer(self) -> None:
        fp = open(self.csv_file, mode="a", newline=self.__newline)
        writer = csv.writer(fp)
        writer.writerows(self.buffer)
        self.buffer = []
        fp.close()

    def write(self, value: Any) -> None:
        fp = open(self.csv_file, mode="a", newline=self.__newline)
        writer = csv.writer(fp)
        writer.writerows(value)
        fp.close()


if __name__ == "__main__":
    status = GL840Configuration(ip="localhost", port=8765)
    daq = DataAcquisition(status, csv_file_base="test", mongo=None,)
    daq.initialize_multi()
    while 1:
        try:
            daq.data_acquire(1)
            print(daq.data.data)
        except KeyboardInterrupt:
            daq.finalize_multi(True)
            break
    daq.finalize_multi(True)
