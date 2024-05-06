#! /usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import BaseServer
import base64
from GL840 import ENCODE
from DocumentBuilder import DocumentBuilder
from typing import Any
import datetime
import random
from DataReader import DataReaderBase


__FORMAT = "%Y-%m-%d %H:%M:%S.%f"


class BasicHandler(BaseHTTPRequestHandler):
    def __init__(self, request: Any, client_address: Any, server: BaseServer, document_builder: DocumentBuilder = DocumentBuilder(), username: str | None = None, password: str | None = None) -> None:
        super().__init__(request, client_address, server)
        self.builder = document_builder
        if (username is None) or (password is None):
            self.code = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode(ENCODE)).decode(ENCODE)

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

    def do_GET(self) -> None:
        if (not self.authenticate()):
            return
        self.send_response(200)
        self.send_header("User-Agent", "test1")
        self.end_headers()
        self.wfile.write("Success".encode(ENCODE))


class RandomDataGenerator(DataReaderBase):
    def __init__(self, num_data: int, random_seed: int = 0) -> None:
        self.random_gen = random.Random(random_seed)
        self.num_data = num_data

    def Read(self) -> list[str]:
        ret = []
        for i in range(self.num_data):
            ret.append(str(self.random_gen.uniform(-100, 100)))
        return ret


class ServerSimulator(BasicHandler):
    def __init__(self, request: Any, client_address: Any, server: BaseServer, data_reader: DataReaderBase, document_builder: DocumentBuilder = DocumentBuilder(), username: str | None = None, password: str | None = None) -> None:
        super().__init__(request, client_address, server, document_builder, username, password)
        self.data_reader = data_reader
        self.line = self.data_reader.Read()
        self.last_time = datetime.datetime.strptime(self.line[0], __FORMAT)

    def __closeFile(self) -> None:
        del self.data_reader

    def do_GET(self) -> None:
        if (not self.authenticate()):
            return
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.last_time < datetime.datetime.now():
            self.line = self.data_reader.Read()
            self.last_time = datetime.datetime.strptime(self.line[0], __FORMAT)
        self.wfile.write(self.builder.buildDocument().encode(ENCODE))

    def __del__(self) -> None:
        self.__closeFile()


if __name__ == "__main__":
    server_address = ("localhost", 6765)
    h = ServerSimulator(("localhost", 6765), ("localhost", 6765), HTTPServer, RandomDataGenerator(28))
    s = HTTPServer(server_address, h)

    s.serve_forever()
