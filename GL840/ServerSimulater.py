#! /usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import base64
from GL840 import ENCODE, TIME_FORMAT
from DocumentBuilder import DocumentBuilder, ValueContainer
from typing import Any
import datetime
import random
from DataReader import DataReaderBase


class BasicHandler(BaseHTTPRequestHandler):
    def __init__(self, document_builder: DocumentBuilder = DocumentBuilder(), username: str | None = None, password: str | None = None) -> None:
        self.builder = document_builder
        if (username is not None) and (password is not None):
            self.code = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode(ENCODE)).decode(ENCODE)
        else:
            self.code = None

    def do_AUTHHEAD(self) -> None:
        self.send_response(401)
        self.send_header("WWW-Authenticate", f'Basic charset="{ENCODE}"')
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_HEAD(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def authenticate(self) -> bool:
        if self.code is None:
            return True
        if self.headers.get('Authorization') is None:
            self.do_AUTHHEAD()
            self.wfile.write(bytes('no auth header received', ENCODE))
            return False
        elif self.headers.get('Authorization') == self.code:
            return True
        else:
            self.do_AUTHHEAD()
            self.wfile.write(bytes('not authenticated', ENCODE))
            return False

    def __call__(self, request: Any, client_address: Any, server: Any) -> Any:
        return super().__init__(request, client_address, server)

    def do_GET(self) -> None:
        if (not self.authenticate()):
            self.send_response(401)
            self.send_header("User-Agent", "test1")
            self.end_headers()
            self.wfile.write("Unauthorized".encode(ENCODE))
            return
        self.send_response(200)
        self.send_header("User-Agent", "test1")
        self.end_headers()
        self.wfile.write("Success".encode(ENCODE))


class RandomDataGenerator(DataReaderBase):
    def __init__(self, num_data: int, random_seed: int = 0, irregular_rate: float = -1.) -> None:
        self.random_gen = random.Random()
        self.random_gen.seed(random_seed)
        self.num_data = num_data
        self.irregular_rate = irregular_rate

    def Read(self) -> list[str | float]:
        ret = []
        ret.append(str(datetime.datetime.now()))
        for i in range(self.num_data):
            if self.irregular_rate > 0:
                ran = self.random_gen.random()
                if ran < self.irregular_rate / 2:
                    ret.append("+++++++")
                    continue
                elif ran < self.irregular_rate:
                    ret.append("Off")
                    continue
            ret.append(self.random_gen.uniform(-100, 100))
        return ret


class ServerSimulator(BasicHandler):
    def __init__(self, data_reader: DataReaderBase, document_builder: DocumentBuilder = DocumentBuilder(), username: str | None = None, password: str | None = None) -> None:
        super().__init__(document_builder, username, password)
        self.data_reader = data_reader
        line = self.data_reader.Read()
        if type(line[0]) is str:
            self.last_time = datetime.datetime.strptime(line[0], TIME_FORMAT)
        else:
            raise ValueError(f"The first column must be str")
        self.line = line[1:]

    def __closeFile(self) -> None:
        del self.data_reader

    def do_GET(self) -> None:
        if (not self.authenticate()):
            self.send_response(401)
            self.send_header("User-Agent", "test1")
            self.end_headers()
            self.wfile.write("Unauthorized".encode(ENCODE))
            return
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.last_time < datetime.datetime.now():
            line = self.data_reader.Read()
            if type(line[0]) is str:
                self.last_time = datetime.datetime.strptime(line[0], TIME_FORMAT)
            else:
                raise ValueError(f"The first column must be str")
            self.line = line[1:]
            self.builder.SetItems(self.last_time, self.line)
        self.wfile.write(self.builder.buildDocument().encode(ENCODE))

    def __del__(self) -> None:
        self.__closeFile()


if __name__ == "__main__":
    server_address = ("localhost", 6765)
    h = ServerSimulator(data_reader=RandomDataGenerator(28, irregular_rate=0.1), document_builder=DocumentBuilder(ValueContainer()), username="GL840", password="GL840")
    s = HTTPServer(server_address, h)
    s.serve_forever()
