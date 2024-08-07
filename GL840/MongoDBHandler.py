"""
mongoDB_handler
==

Mongo DB interface for HSQuickLook.

Classes
--

MongoDBSections, MongoDBData
    The pushed data into MongoDB.
MongoDBPusher
    Push the data into MongoDB.

"""
import datetime
from time import time
from typing import Any, Optional
from pymongo import mongo_client

TI_RATE = 64


def convert2ti(unixtime: float) -> int:
    ti = int(unixtime * TI_RATE)
    return ti


def convert2unixtime(ti: int) -> float:
    return float(ti) / float(TI_RATE)


class MongoDBSection():
    """
    Section structure for HSQuickLook.

    Attributes
    --

    section : str
        Section Name.
    contents : dict[str, Any]
        Input data. The key of the dictionary means the name of data and must be string type.

    Examples
    --

        (1) Initialize the instance.

            >>> sec = MongoDBSection("section name", {"Time": datetime.now(), "Voltage": 10})

        (2) If you call this instance, it returns dict data for HSQuickLook.

            >>> print(sec())
            {"__section__": "section name", "__contents__": {"Time": datetime.now(), "Voltage": 10}}

    """

    def __init__(self, section: str, contents: dict[str, Any]) -> None:
        """
        Section structure for HSQuickLook.

        Parameters
        --

        section : str
            Section Name.
        contents : dict[str, Any]
            Input data. The key of the dictionary means the name of data and must be string type.
        """
        self.section = section
        self.contents = contents

    def __call__(self) -> dict[str, Any]:
        """
        If the instance is called, returns data converted for HSQuickLook.

        Parameters
        --

        None

        Returns
        --

        data : dict[str, Any]:
            Converted data for HSQuickLook.

        """
        return {"__section__": self.section, "__contents__": self.contents}


class MongoDBData():
    """
    Data structure for HSQuickLook.

    Attributes
    --

    directory : str
        The directory name.
    document : str
        The document name.
    sections : list[MongoDBSection]
        MongoDB sections.
    unixtime : int | datetime, Optional
        Unix time. If none, use the current time.

    Examples
    --

        (1) Initialize the instance.

            >>> data = MongoDBData("directory", "document", 6400000, 100000, [sec,])

        (2) If you call this instance, it returns dict data for HSQuickLook.

            >>> print(data())

    See Also
    --

        MongoDBSection
    """

    def __init__(self, directory: str, document: str, sections: list[MongoDBSection], unixtime: Optional[float | datetime.datetime] = None, ti: int | None = None) -> None:
        """
        Data structure for HSQuickLook.

        Parameters
        --

        directory : str
            The directory name.
        document : str
            The document name.
        ti : int
            Time indexer.
        unixtime : int
            Unix time.
        sections : list[MongoDBSection]
            MongoDB sections.

        Returns
        --

        None
        """
        self.directory = directory
        self.document = document
        if unixtime is None:
            self.unixtime = time()
        elif isinstance(unixtime, float):
            self.unixtime = unixtime
        else:
            self.unixtime = int(unixtime.timestamp())
        if ti is None:
            self.ti = convert2ti(self.unixtime)
        else:
            self.ti = ti
        self.sections = sections

    def __call__(self) -> dict[str, Any]:
        """
        If the instance is called, returns data converted for HSQuickLook.

        Parameters
        --

        None

        Returns
        --

        data : dict[str, Any]:
            Converted data for HSQuickLook.

        """
        return {"__directory__": self.directory, "__document__": self.document, "__ti__": self.ti, "__unixtime__": self.unixtime, "__sections__": [section() for section in self.sections]}


class MongoDBPusher():
    """
    Push the data into MongoDB.

    Attributes
    --
    client : mongo_client.MongoClient
        The client object of MongoDB.
    dbs : mongo_client.database.DataBase
        The database object push the data into.
    collec : pymongo.collection.Collection
        The collection object push the data into.

    Methods
    --
    put(data: MongoDBData):
        Put the data into database.
    """

    def __init__(self, ip: Optional[str] = None, port: Optional[int] = None, database: str = "GL840", collection: str = "GL840") -> None:
        """
        Push the data into MongoDB.

        Parameters
        --

        ip : Optional[str]
            Ip address of MongoDB. If None, the  ip address is set to default value.
        port : Optional[int]
            Port of MongoDB. If None, the port is set to default value.
        database : str, default "GL840"
            Database name.
        collection : str, default "GL840"
            Collection name.

        Returns
        --

        None
        """
        self.client: mongo_client.MongoClient = mongo_client.MongoClient(ip, port)
        assert self.client is not None
        self.dbs = self.client[database]
        self.collec = self.dbs[collection]

    def push(self, data: MongoDBData) -> None:
        """
        Push the data into the database.

        Parameter
        --

        data : MongoDBData
            The MongoDBData object push into the database.

        Returns
        --

        None
        """
        self.collec.insert_one(data())


class MongoDBPuller():
    def __init__(self, ip: Optional[str] = None, port: Optional[int] = None, database: str = "GL840", collection: str = "GL840") -> None:
        """
        Push the data into MongoDB.

        Parameters
        --

        ip : Optional[str]
            Ip address of MongoDB. If None, the  ip address is set to default value.
        port : Optional[int]
            Port of MongoDB. If None, the port is set to default value.
        database : str, default "GL840"
            Database name.
        collection : str, default "GL840"
            Collection name.

        Returns
        --

        None
        """
        self.client = mongo_client.MongoClient(ip, port)
        assert self.client is not None
        self.dbs = self.client[database]
        self.collec = self.dbs[collection]

    def pull_one(self, directory: str | None = None, document: str | None = None, filter: dict[str, Any] = {}) -> MongoDBData | None:
        """
        Pull the latest data from the MongoDB.

        Parameters
        --

        directory : str | None (Default None)
            The directory name. If None, the latest data independent on directory is pulled.
        document : str | None (Default None)
            The document name. If None, the latest data independent on document is pulled.
        filter: dict[str, Any] (Default {})
            The filter for the MongoDB.

        Returns
        --

        data : MongoDBData | None
            The latest data pulled from the MongoDB. If None, the data is not found.
        """
        if directory is not None:
            filter["__directory__"] = directory
        if document is not None:
            filter["__document__"] = document
        ret = self.collec.find(filter).sort({"_id": -1}).limit(1)[0]
        if ret is not None:
            ti = ret["__ti__"]
            directory_ret = ret["__directory__"]
            document_ret = ret["__document__"]
            sections = ret["__sections__"]
            _sections = []
            for i in range(len(sections)):
                name = sections[i]["__section__"]
                contents = sections[i]["__contents__"]
                sec = MongoDBSection(name, contents)
                _sections.append(sec)
            return MongoDBData(directory_ret, document_ret, _sections, convert2unixtime(ti), ti)
        else:
            return None
