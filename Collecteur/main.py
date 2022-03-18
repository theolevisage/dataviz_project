import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host = '172.20.0.10'
port = 65432
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from time import sleep
# import socket

# HOST = "172.20.0.11"  # Standard loopback interface address (localhost)
# PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


# if __name__ == '__main__':
#     while True:
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             s.bind((HOST, PORT))
#             s.listen()
#             conn, addr = s.accept()
#             with conn:
#                 print(f"Connected by {addr}")
#                 while True:
#                     data = conn.recv(1024)
#                     if not data:
#                         break
#                     conn.sendall(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
