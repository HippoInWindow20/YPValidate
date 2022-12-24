# from flask import Flask, request
# 
# app = Flask(__name__)


# @app.route('/', methods=['POST'])
# def result():
    # print(request.form['foo'])
    # ocr = ddddocr.DdddOcr(beta=True)
    # with open("https://lds.yphs.tp.edu.tw/tea/validatecode.aspx", 'rb') as f:
        # image = f.read()
    # res = ocr.classification(image)
    # return res.upper()  # response to your request.

from http.server import BaseHTTPRequestHandler, HTTPServer # python3
import ddddocr
import requests
from urllib.parse import urlparse
class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        # try:
            self._set_headers()
        
            query = urlparse(self.path).query
            # query_components = dict(qc.split("=") for qc in query.split("&"))
            # cookie = query_components["cookie"]
            print(query)
            ocr = ddddocr.DdddOcr(beta=True)
            response = requests.get("https://lds.yphs.tp.edu.tw/tea/validatecode.aspx")
            res = ocr.classification(response.content)
            self.wfile.write(res.upper().encode())
        # except:
        #     self._set_headers()
        #     self.wfile.write("error".encode())

host = ''
port = 80
HTTPServer((host, port), HandleRequests).serve_forever()
print("serving...")