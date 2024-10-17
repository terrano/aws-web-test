import socket
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Function to get the server's IP address
def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        ip_address = get_ip_address()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f"Your IP address is: {ip_address}".encode())

# Run the server on port 3000
def run(server_class=HTTPServer, handler_class=MyHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

run()

