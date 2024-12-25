#! /usr/bin/env python3

from .DataAnalyzer import DataAnalyzer as Analyzer
import glob
import re
import datetime as dt
import os.path


class MultiDataAnalyzer():
    def __init__(self, glob_pattern: str, quiet: bool = False) -> None:
        mat = re.fullmatch(r"(.*/.*)_\d.csv", os.path.expanduser(glob_pattern))
        if mat is None:
            glob_pattern += r"/*_0.csv"
        else:
            glob_pattern = mat.group(1) + r"_0.csv"
        file_iter = glob.glob(glob_pattern, recursive=True)
        __filelist = sorted(file_iter, key=MultiDataAnalyzer.__key_func)
        self.__filelist = list(map(lambda x: x.replace("_0.csv", ""), __filelist))
        self.__quiet = quiet
        if not self.__quiet:
            print("Top File list:")
            print(self.__filelist)
        self.__analyzer: Analyzer | None = Analyzer(self.__filelist.pop(0), quiet=True)

    @staticmethod
    def __key_func(x: str) -> str:
        ret = x.split("/")[-2] + x.split("/")[-1]
        return ret

    def __goto_next_analyzer(self) -> None:
        try:
            if not self.__quiet:
                print(f"Going to next analyzer: {self.__filelist[0]}")
            self.__analyzer = Analyzer(self.__filelist.pop(0), quiet=True)
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self

    def __next__(self) -> dict[str, float | dt.datetime | None]:
        if self.__analyzer is None:
            raise StopIteration
        try:
            ret = next(self.__analyzer)
        except StopIteration:
            while True:
                self.__goto_next_analyzer()
                if self.__analyzer is None:
                    raise StopIteration
                try:
                    ret = next(self.__analyzer)
                    break
                except StopIteration:
                    pass
        return ret
