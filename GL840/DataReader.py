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


class DataReaderBase:
    def __init__(self) -> None:
        pass

    def Read(self) -> list[str]:
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

    def ReadLine(self) -> list[str]:
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
        return text

    def Read(self) -> list[str]:
        return self.ReadLine()

    def __del__(self) -> None:
        self.__fp.close()


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

    def ReadLine(self) -> list[str]:
        text = super().ReadLine()
        if text == "":
            self.__fileindex += 1
            if self.__fileindex >= self.numfile:
                self.__fileindex = 0
            self.__openFile()
            text = super().ReadLine()
        return text

    def Read(self) -> list[str]:
        return self.ReadLine()
