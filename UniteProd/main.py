import socket
import json

ClientMultiSocket = socket.socket()
host = '172.20.0.10'
port = 65432
print('Waiting for connection response')
m = b'{"id": 2, "name": "abc"}'
jsonObj = json.loads(m)
data = jsonObj

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:
    ClientMultiSocket.send(m)
    received = ClientMultiSocket.recv(1024)
    print(f"Sent:     {json.loads(m)}")
    print(f"Received: {json.loads(received)}")
ClientMultiSocket.close()
