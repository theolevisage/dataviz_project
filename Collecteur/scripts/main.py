import socket
import mysql.connector as mariadb
from datetime import datetime
from _thread import *
import time
import json
import gnupg

gpg = gnupg.GPG('/usr/bin/gpg')
gpg.encoding = 'utf-8'

time.sleep(10)

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


def connect_to_db():
    return mariadb.connect(
        host="mariadb",
        port=3306,
        user="root",
        password="root123",
        database="datas")


def insert_automats_data(dict_data):
    try:
        conn = connect_to_db()
        conn.autocommit = False
        cursor = conn.cursor()

        for automat in dict_data['automats']:
            cursor.execute(
                "INSERT INTO automat (unite_number, created_at, automat_type, automat_number, tank_temp, ext_temp, milk_weight, ph, kplus, nacl, salmonella, e_coli, listeria) VALUES (%s, TIMESTAMP(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (dict_data['unite_number'], datetime.fromisoformat(dict_data['created_at']), automat['automat_type'],
                 automat['automat_number'], automat['tank_temp'], automat['ext_temp'], automat['milk_weight'],
                 automat['ph'], automat['kplus'], automat['nacl'], automat['salmonella'], automat['e_coli'],
                 automat['listeria'])
            )

        conn.commit()
        print('automats datas inserted')

    except mariadb.Error as error_mariadb:
        print("Failed to update record to database rollback: {}".format(error_mariadb))
        # reverting changes because of exception
        conn.rollback()
    finally:
        # closing database connection.
        if conn.is_connected():
            cursor.close()
            conn.close()


def insert_public_key(secure_payload):
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO pub_key (unite_number, pub_key) VALUES (%s, %s)",
            (secure_payload['unite_number'], secure_payload['public_key'])
        )

        conn.commit()
        print('public key inserted')

    except mariadb.Error as error_mariadb:
        print("Failed to update record to database rollback: {}".format(error_mariadb))
        # reverting changes because of exception
    finally:
        # closing database connection.
        if conn.is_connected():
            cur.close()
            conn.close()


def check_proof(sended_proof, created_at):
    datetime_created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
    stamp = datetime.timestamp(datetime_created_at)
    xor = int(stamp) ^ 10000
    needed_proof = xor << 2
    print('sended_proof : ' + str(sended_proof))
    print('needed_proof : ' + str(needed_proof))
    return sended_proof == needed_proof


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048 * 4)
        if data:
            dict_data = convert_byte_to_dict(data)
            key = 'public_key'
            if(key in dict_data):
                insert_public_key(dict_data)
                collector_key = gpg.export_keys('name <mail@example.com>')
                payload = {
                    "name": "collector",
                    "public_key": collector_key
                }
                data = json.dumps(payload).encode('utf-8')
            else:
                if check_proof(dict_data['proof'], dict_data['created_at']):
                    print('proof match, insert datas in db')
                    insert_automats_data(dict_data)
                else:
                    print('proof does not match, dont insert datas')
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
