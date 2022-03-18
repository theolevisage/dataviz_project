import socket
import mysql.connector as mariadb
from datetime import datetime
from _thread import *

# insert information
conn = mariadb.connect(
    user="root",
    password="root123",
    host="172.20.0.9",
    port="3306",
    database="datas")
cur = conn.cursor()

cur.execute("SELECT unite_number FROM automats")

for unite_number in cur:
    print(f"unite_number: {unite_number}")

conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")

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
        data = connection.recv(2048*4)
        if not data:
            break
        connection.sendall(data)
    connection.close()


while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
conn.close()
