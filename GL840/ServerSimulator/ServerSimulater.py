#! /usr/bin/env python3
from _socket import _RetAddress
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import BaseServer
import base64
from DocumentBuilder import DocumentBuilder
from typing import Any
import pathlib
import time


class BasicHandler(BaseHTTPRequestHandler):
    def __init__(self, request: Any, client_address: Any, server: BaseServer, document_builder: DocumentBuilder = DocumentBuilder(), username: str | None = None, password: str | None = None) -> None:
        super().__init__(request, client_address, server)
        self.builder = document_builder
        if (username is None) or (password is None):
            self.code = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')

    def do_AUTHHEAD(self) -> None:
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic charset="UTF-8"')
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_HEAD(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def authenticate(self) -> bool:
        if self.headers.get('Authorization') is None:
            self.do_AUTHHEAD()
            self.wfile.write(bytes('no auth header received', 'utf-8'))
            return False
        elif self.headers.get('Authorization') == self.code:
            return True
        else:
            self.do_AUTHHEAD()
            self.wfile.write(bytes('not authenticated', 'utf-8'))
            return False

    def do_GET(self) -> None:
        if (not self.authenticate()):
            return
        self.send_response(200)
        self.send_header("User-Agent", "test1")
        self.end_headers()
        html = self.builder.buildDocument()
        self.wfile.write(html.encode())


class ServerSimulator(BasicHandler):
    def __init__(self, request: _RetAddress, client_address: _RetAddress, server: BaseServer, directory: str, filename_base: str, file_extension: str = ".csv", document_builder: DocumentBuilder = DocumentBuilder(), username: str | None = None, password: str | None = None) -> None:
        super().__init__(request, client_address, server, document_builder, username, password)
        self.numfile = len(tuple(pathlib.Path(directory).glob(f"{filename_base}*{file_extension}")))
        self.directory = directory
        self.filename_base = filename_base
        self.filename_extension = file_extension
        self.__fileindex = 0
        self.__Time = time.time()
        self.__openFile()

    def __openFile(self) -> None:
        self.filename = self.directory + "/" + self.filename_base + str(self.__fileindex) + self.filename_extension
        self.fp = open(self.filename, "r")

    def __closeFile(self) -> None:
        self.fp.close()

    def __del__(self) -> None:
        self.__closeFile()


if __name__ == "__main__":
    server_address = ("localhost", 6765)
    h = BasicHandler
    s = HTTPServer(server_address, h)
    s.serve_forever()
