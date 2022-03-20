import socket
import mysql.connector as mariadb
from datetime import datetime
from _thread import *
import sys
import time
import json

time.sleep(10)
# insert information

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


def convert_byte_to_dict(binary_data):
    str_data = binary_data.decode("UTF-8")
    return json.loads(str_data)


def insert_in_db(dict_data):
    for automat in dict_data['automats']:
        conn = mariadb.connect(
            host="mariadb",
            port=3306,
            user="root",
            password="root123",
            database="datas")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO automats (unite_number, created_at, automat_type, automat_number, tank_temp, ext_temp, milk_weight, ph, kplus, nacl, salmonella, e_coli, listeria) VALUES (%s, TIMESTAMP(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (dict_data['unite_number'], datetime.fromisoformat(dict_data['created_at']), automat['automat_type'],
             automat['automat_number'], automat['tank_temp'], automat['ext_temp'], automat['milk_weight'],
             automat['ph'], automat['kplus'], automat['nacl'], automat['salmonella'], automat['e_coli'],
             automat['listeria'])
        )
        conn.commit()
        cur.close()
        conn.close()

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048 * 4)
        if data:
            insert_in_db(convert_byte_to_dict(data))
        else:
            break
        connection.sendall(data)
    connection.close()


while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
conn.close()
