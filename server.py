import BaseHTTPServer
import os
import time

HOST_NAME = 'localhost'
PORT_NUM = 4242

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_HEAD(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
  
  def do_GET(self):
    self.path = os.getcwd() + '/index.html'
    try:
      with open(self.path) as f:
        content = f.read()
        self.do_HEAD()
        self.wfile.write(content)
    except IOError:
      print 'Not found!!!'
      self.send_error(404)    

if __name__ == '__main__':
  server_class = BaseHTTPServer.HTTPServer
  httpd = server_class((HOST_NAME, PORT_NUM), Handler)
  print '<Ctrl-c> to exit'
  print time.asctime(), 'Server starts - {}:{}'.format(HOST_NAME, PORT_NUM)
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass
  httpd.server_close()