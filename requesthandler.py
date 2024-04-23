from http.server import BaseHTTPRequestHandler, HTTPServer
from datahandler import DataHandler
from urllib.parse import urlparse, parse_qs
import json
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            handler = DataHandler("./data/artisteDevoir.xml")
            all_data=handler.retreive_all_data()
            html_content=handler.generate_html(all_data)

            self.wfile.write(bytes(html_content, "utf8"))
            # json_data = json.dumps(all_data)
    
            
            # json_bytes = json_data.encode("utf8")
            
           
            # self.wfile.write(json_bytes)
        elif self.path.startswith('/filter'):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            artist_name = query.get('artist_name', [''])[0]
            print("artistname :",artist_name)
            handler = DataHandler("./data/artisteDevoir.xml")
            all_data = handler.retrieve_filtered_data(artist_name)
            filtered_content=handler.generate_html(all_data)
            if(len(filtered_content)==0):
                filtered_content="No artist found"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            
            
            self.wfile.write(bytes(filtered_content, "utf8"))
            # json_data = json.dumps(all_data)
    
            
            # json_bytes = json_data.encode("utf8")
            
           
            # self.wfile.write(json_bytes)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("404 Not Found", "utf8"))

