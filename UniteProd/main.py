import socket
ClientMultiSocket = socket.socket()
host = '172.20.0.10'
port = 65432
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:
    Input = input('Hey there: ')
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()




# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from time import sleep
# import socket
# import json

# HOST = "172.20.0.10"  # Standard loopback interface address (localhost)
# PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# m = b'{"id": 2, "name": "abc"}'
# jsonObj = json.loads(m)
# data = jsonObj

# if __name__ == '__main__':
#     while True:
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             print("BEFORE CONNECT")
#             s.connect(("172.20.0.10", 65432))
#             print("AFTER CONNECT")
#             s.sendall(m)
#             received = s.recv(1024)

#         print(f"Sent:     {json.loads(m)}")
#         print(f"Received: {json.loads(received)}")
#         sleep(5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
