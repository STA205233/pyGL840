#! /usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("User-Agent", "test1")
        self.end_headers()
        html = "<b>&nbsp;+ 20.6</b><b>&nbsp;- 21.0</b><b>&nbsp;+ 1.2</b><b>&nbsp;+ 1.2</b>" + "<b>&nbsp;Off</b><b>&nbsp;Off</b>" * 8
        self.wfile.write(html.encode())


if __name__ == "__main__":
    server_address = ("localhost", 6765)
    h = Handler
    s = HTTPServer(server_address, h)
    s.serve_forever()
