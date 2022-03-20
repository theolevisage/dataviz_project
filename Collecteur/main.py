import socket
import mysql.connector as mariadb
from datetime import datetime
from _thread import *
import sys
import time

time.sleep(20)
# insert information
try:
    conn = mariadb.connect(
        host="mariadb",
        port=3306,
        user="root",
        password="root123",
        database="datas")
    cur = conn.cursor()
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur.execute("INSERT INTO automats (unite_number, created_at, automat_type, automat_number, tank_temp, ext_temp, milk_weight, ph, kplus, nacl, salmonella, e_coli, listeria) VALUES (%s, TIMESTAMP(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (1, datetime.now(), 1, 1, 0.1, 0.1, 1, 0.1, 1, 0.1, 1, 1, 1))


conn.commit()
print(f"Last Inserted ID: {cur.lastrowid}")

ServerSideSocket = socket.socket()
host = 'collector'
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
