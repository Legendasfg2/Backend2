from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/hello":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, world!")

        elif self.path == "/time":
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(now.encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

if __name__ == "__main__":
    server_address = ("", 8000)  # порт 8000
    httpd = HTTPServer(server_address, MyHandler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()
