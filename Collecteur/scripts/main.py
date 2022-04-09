import socket
import mysql.connector as mariadb
from os.path import exists
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


def convert_data(binary_data):
    str_data = binary_data.decode("UTF-8")
    try:
        data = json.loads(str_data)
    except:
        data = str_data
    finally:
        return data


def connect_to_db():
    return mariadb.connect(
        host="mariadb",
        port=3306,
        user="root",
        password="root123",
        database="datas")


def insert_automats_data(dict_data):
    data_inserted = False
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
        data_inserted = True
        print('automats datas inserted')
    except mariadb.Error as error_mariadb:
        print("Failed to update record to database rollback: {}".format(error_mariadb))
        conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        return data_inserted


def insert_public_key(secure_payload):
    path_public_unit_key = '../.keys/unit_' + secure_payload['unite_number'] + '.gpg'
    file_exists = exists(path_public_unit_key)
    if not file_exists:
        f = open(path_public_unit_key, 'x')
        f.write(secure_payload['public_key'])
        f.close()
        f = open(path_public_unit_key, 'r')
        import_result = gpg.import_keys(f.read())
        gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE')
        f.close()


def check_proof(sended_proof, created_at):
    datetime_created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
    stamp = datetime.timestamp(datetime_created_at)
    xor = int(stamp) ^ 10000
    needed_proof = xor << 2
    return sended_proof == needed_proof


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048 * 4)
        if data:
            dict_data = convert_data(data)
            key = "public_key"
            if(key in dict_data):
                insert_public_key(dict_data)
                collector_key = gpg.export_keys('collector <collector@mail.com>')
                payload = {
                    "name": "collector",
                    "public_key": collector_key
                }
            else:
                decrypted_data = gpg.decrypt(dict_data)
                dict_data = convert_data(decrypted_data.data)
                if check_proof(dict_data['proof'], dict_data['created_at']):
                    print('proof match, insert datas in db')
                    data_inserted = insert_automats_data(dict_data)
                else:
                    print('proof does not match, dont insert datas')
                    # for security reason we send true when proof does not match
                    data_inserted = True
                payload = {
                    "name": "collector",
                    "data_inserted": data_inserted,
                    "datetime": dict_data['created_at']
                }
            data = json.dumps(payload).encode('utf-8')
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
