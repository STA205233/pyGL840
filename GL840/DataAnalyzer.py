#! /usr/bin/env python3
import datetime as dt
from typing import TextIO
import glob


class DataAnalyzer():
    def __init__(self, filename_header: str) -> None:
        self.__fp: TextIO | None = None
        self.__filenames = sorted(glob.glob(filename_header + "*.csv"), key=lambda x: int(x.split("_")[-1].split(".")[0]))
        print(self.__filenames)
        self.__header: list[str] = []
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self) -> dict[str, float | dt.datetime | None]:
        if self.__fp is None:
            self.__fp = open(self.__filenames[0], "r")
            self.__header = self.__fp.readline().split(",")
        data = self.__get_data()
        if data is None:
            self.__index += 1
            if self.__index >= len(self.__filenames):
                raise StopIteration
            self.__fp = open(self.__filenames[self.__index], "r")
            self.__header = self.__fp.readline().split(",")
            data = self.__get_data()
            if data is None:
                raise StopIteration
        return data

    def __get_data(self) -> dict[str, float | dt.datetime | None] | None:
        if self.__fp is None:
            raise ValueError("File is not opened.")
        line = self.__fp.readline()
        if line == "":
            self.__fp.close()
            self.__fp = None
            return None
        list_line = line.split(",")
        try:
            time = dt.datetime.strptime(list_line[0], "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            time = dt.datetime.strptime(list_line[0], "%Y-%m-%d %H:%M:%S")
        except Exception:
            raise ValueError(f"Time format ({list_line[0]} in {self.__fp.name}) is not correct.")
        dic: dict[str, float | dt.datetime | None] = {"Time": time}
        for i, name in enumerate(self.__header[1:]):
            try:
                dic[name] = float(list_line[i + 1])
            except ValueError:
                dic[name] = None
        return dic


if __name__ == "__main__":
    analyzer = DataAnalyzer("filename")
    x = []
    y = []
    for data in analyzer:
        x.append(data["Time"])
        y.append(data["Ch1"])
        print(x, y)
