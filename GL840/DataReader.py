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


class DataReader:
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

    def ReadLine(self) ->
