from requesthandler import RequestHandler
from http.server import HTTPServer

def run_server():
    print('Starting server...')
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running at http://localhost:8080')
    httpd.serve_forever()

# Call the function to start the server
run_server()