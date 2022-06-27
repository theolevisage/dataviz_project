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

proof_config = {
    "1": {
        "decalage": 1,
        "exposant": 1000
    },
    "2": {
        "decalage": 2,
        "exposant": 2000
    },
    "3": {
        "decalage": 3,
        "exposant": 3000
    },
    "4": {
        "decalage": 4,
        "exposant": 4000
    },
    "5": {
        "decalage": 5,
        "exposant": 5000
    }
}

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


def is_data_correct(dict_data):
    errors = []
    for automat in dict_data['automats']:
        automat_errors = []
        if not 1 <= int(automat['automat_number']) <= 10:
            automat_errors.append(automat['automat_number'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR automat_number : ')
            print(automat['automat_number'])

        if not 1 <= int(automat['automat_type']) <= 15:
            automat_errors.append(automat['automat_type'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR automat_type : ')
            print(automat['automat_type'])

        if not 2.5 <= float(automat['tank_temp']) <= 4:
            automat_errors.append(automat['tank_temp'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR automat_type : ')
            print(automat['automat_type'])

        if not 8 <= float(automat['ext_temp']) <= 14:
            automat_errors.append(automat['ext_temp'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR ext_temp : ')
            print(automat['ext_temp'])

        if not 3512 <= int(automat['milk_weight']) <= 4607:
            automat_errors.append(automat['milk_weight'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR milk_weight : ')
            print(automat['milk_weight'])

        if not 6.8 <= float(automat['ph']) <= 7.2:
            automat_errors.append(automat['ph'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR ph : ')
            print(automat['ph'])

        if not 35 <= int(automat['kplus']) <= 47:
            automat_errors.append(automat['kplus'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR kplus : ')
            print(automat['kplus'])

        if not 1 <= float(automat['nacl']) <= 1.7:
            automat_errors.append(automat['nacl'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR nacl : ')
            print(automat['nacl'])

        if not 17 <= int(automat['salmonella']) <= 37:
            automat_errors.append(automat['salmonella'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR salmonella : ')
            print(automat['salmonella'])

        if not 35 <= int(automat['e_coli']) <= 49:
            automat_errors.append(automat['e_coli'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR e_coli : ')
            print(automat['e_coli'])

        if not 28 <= int(automat['listeria']) <= 54:
            automat_errors.append(automat['listeria'])
            print('ERROR for unit_number : ')
            print(dict_data['unit_number'])
            print('ERROR listeria : ')
            print(automat['listeria'])
        if len(automat_errors) > 0:
            errors.append(automat_errors)
    return not errors


def insert_anomalies(dict_data):
    data_inserted = False
    try:
        conn = connect_to_db()
        conn.autocommit = False
        cursor = conn.cursor()

        datenow = datetime.now()
        occurence_date = datenow.isoformat()

        for automat in dict_data['automats']:
            cursor.execute(
                "INSERT INTO anomaly (occurence_date, unit_number, created_at, automat_type, automat_number, tank_temp, ext_temp, milk_weight, ph, kplus, nacl, salmonella, e_coli, listeria) VALUES (TIMESTAMP(%s), %s, TIMESTAMP(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (occurence_date, dict_data['unit_number'], datetime.fromisoformat(dict_data['created_at']), automat['automat_type'],
                 automat['automat_number'], automat['tank_temp'], automat['ext_temp'], automat['milk_weight'],
                 automat['ph'], automat['kplus'], automat['nacl'], automat['salmonella'], automat['e_coli'],
                 automat['listeria'])
            )
        conn.commit()
        data_inserted = True
        print('anomalies inserted')
    except mariadb.Error as error_mariadb:
        print("Failed to insert anomalies to database rollback: {}".format(error_mariadb))
        conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        return data_inserted


def insert_automats_data(dict_data):
    data_inserted = False
    try:
        conn = connect_to_db()
        conn.autocommit = False
        cursor = conn.cursor()

        for automat in dict_data['automats']:
            cursor.execute(
                "INSERT INTO automat (unit_number, created_at, automat_type, automat_number, tank_temp, ext_temp, milk_weight, ph, kplus, nacl, salmonella, e_coli, listeria) VALUES (%s, TIMESTAMP(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (dict_data['unit_number'], datetime.fromisoformat(dict_data['created_at']), automat['automat_type'],
                 automat['automat_number'], automat['tank_temp'], automat['ext_temp'], automat['milk_weight'],
                 automat['ph'], automat['kplus'], automat['nacl'], automat['salmonella'], automat['e_coli'],
                 automat['listeria'])
            )
        conn.commit()
        data_inserted = True
        print('automats datas inserted')
    except mariadb.Error as error_mariadb:
        print("Failed to insert automat datas to database rollback: {}".format(error_mariadb))
        conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        return data_inserted


def insert_production_unit(secure_payload):
    path_public_unit_key = '../.keys/unit_' + secure_payload['unit_number'] + '.gpg'
    f = open(path_public_unit_key, 'w')
    f.write(secure_payload['public_key'])
    f.close()
    f = open(path_public_unit_key, 'r')
    import_result = gpg.import_keys(f.read())
    gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE')
    f.close()

    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO production_unit (unit_number, ban) VALUES (%s, %s)",
            (secure_payload['unit_number'], 0)
        )

        conn.commit()
        print('unit inserted')

    except mariadb.Error as error_mariadb:
        print("Failed to insert production unit to database rollback: {}".format(error_mariadb))
        # reverting changes because of exception
    finally:
        # closing database connection.
        if conn.is_connected():
            cur.close()
            conn.close()


def check_proof(sended_proof, created_at, unit_nb):
    decalage = proof_config[unit_nb]["decalage"]
    exposant = proof_config[unit_nb]["exposant"]
    datetime_created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
    stamp = datetime.timestamp(datetime_created_at)
    xor = int(stamp) ^ exposant
    needed_proof = xor << decalage
    return sended_proof == needed_proof


def is_banned(unit_number):
    is_banned = False;
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT ban FROM production_unit WHERE unit_number = %s",
            (unit_number, )
        )
        is_banned = cursor.fetchone()[0]
    except mariadb.Error as error_mariadb:
        print("Failed to query database : {}".format(error_mariadb))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
        return is_banned


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048 * 4)
        if data:
            dict_data = convert_data(data)
            key = "public_key"
            if(key in dict_data):
                insert_production_unit(dict_data)
                collector_key = gpg.export_keys('collector <collector@mail.com>')
                payload = {
                    "name": "collector",
                    "public_key": collector_key
                }
                data = json.dumps(payload).encode('utf-8')
            else:
                decrypted_data = gpg.decrypt(dict_data)
                dict_data = convert_data(decrypted_data.data)
                data_inserted = True
                unit_number = dict_data['unit_number']
                if not is_banned(unit_number):
                    proof = dict_data['proof']
                    creation_date = dict_data['created_at']
                    if check_proof(proof, creation_date, unit_number):
                        print('proof match, insert datas in db')
                        if is_data_correct(dict_data):
                            data_inserted = insert_automats_data(dict_data)
                        else:
                            data_inserted = insert_anomalies(dict_data)
                    else:
                        print('proof does not match, do not insert datas')
                else:
                    print(str(dict_data['unit_number']), 'is banned')
                    # this machine is banned, special treatment ?
                payload = {
                    "name": "collector",
                    "data_inserted": data_inserted,
                    "datetime": dict_data['created_at']
                }
                encryption_result = gpg.encrypt(json.dumps(payload).encode('utf-8'), 'unit' + dict_data['unit_number'] + '@mail.com')
                data = encryption_result.data

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
