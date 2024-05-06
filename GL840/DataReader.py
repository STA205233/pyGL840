"""
DataReader
==

Read files written by GL840.DataAcquisition.

Classes
--

DataReader:
    Base class for reading data from files.
DataFormat:
    Containing all information.

"""

import pathlib
from GL840 import SPECIAL_VALUE


class DataReaderBase:
    def __init__(self) -> None:
        pass

    def Read(self) -> list[str | float]:
        raise SyntaxError("Class DataReaderBase cannot be used directly.")


class DataReader(DataReaderBase):
    """
    DataReader
    ==

    Base class for reading data from files.

    Attributes
    --

    filename: str
        file name to read.

    Functions
    --

    ReadLine(): str
        Read one line

    """

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.__fp = open(filename, "r")

    def ReadLine(self) -> list[str | float]:
        """
        Read one line

        Arguments
        --

        None

        Returns
        --

        Line: list[str]
            One line of data.

        """

        text = self.__fp.readline().strip().split(",")
        _ret = DataReader.ConvertStr2Float(text)
        return _ret

    def Read(self) -> list[str | float]:
        return self.ReadLine()

    def __del__(self) -> None:
        self.__fp.close()

    @staticmethod
    def ConvertStr2Float(values) -> list[str | float]:
        _ret: list[float | str] = []
        for i in range(1, len(values)):
            if values[i] not in SPECIAL_VALUE:
                _ret[i] = float(values[i])
        return _ret


class DataReaderMultiple(DataReader):
    def __init__(self, directory: str, filename_base: str, file_extension: str = ".csv") -> None:
        self.numfile = len(tuple(pathlib.Path(directory).glob(f"{filename_base}*{file_extension}")))
        self.directory = directory
        self.filename_base = filename_base
        self.filename_extension = file_extension
        self.__fileindex = 0
        super().__init__(directory + "/" + filename_base + "0" + file_extension)

    def __openFile(self) -> None:
        self.filename = self.directory + "/" + self.filename_base + str(self.__fileindex) + self.filename_extension
        self.fp = open(self.filename, "r")

    def ReadLine(self) -> list[str | float]:
        text = super().ReadLine()
        if text == "":
            self.__fileindex += 1
            if self.__fileindex >= self.numfile:
                self.__fileindex = 0
            self.__openFile()
            text = super().ReadLine()
        return text

    def Read(self) -> list[str | float]:
        return self.ReadLine()
