import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Server HTTP on prot %s...'%PORT)

def Processing(req):
  uid = req.split("key=")[1].split(" ")[0]
  return uid

class Rec:
  def process(self, req):
    uid = req.split("key=")[1].split(" ")[0]
    return self.rec(uid)
  def rec(self, uid):
    rec = "1231, 123123, 21313"
    return rec

r = Rec()

while True:
  client_connection, client_address = listen_socket.accept()
  req = client_connection.recv(1024)
  print("***")
  print(Processing(req))
  print(r.process(req))
  print("***")

  http_response = """
HTTP/1.1 200 OK

Hello, World!
"""
  print(http_response)
  client_connection.sendall(http_response)
  client_connection.close()
