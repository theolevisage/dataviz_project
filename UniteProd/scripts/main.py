import os
import socket
import json
import random
import time
from datetime import datetime
from os.path import exists
import gnupg

gpg = gnupg.GPG('/usr/bin/gpg')
gpg.encoding = 'utf-8'
init = True
unite_number = os.getenv('UNITE_NUMBER')
name = os.getenv('NAME')
mail = os.getenv('MAIL')
unit_public_key = gpg.export_keys(name + ' <' + mail + '>')
automat_types = [13, 12, 15, 9, 8, 2, 6, 8, 5, 2]
time.sleep(10)


def convert_data(binary_data):
    str_data = binary_data.decode("UTF-8")
    try:
        data = json.loads(str_data)
    except:
        data = str_data
    finally:
        return data

while True:
    if (init):
        datas = {
            "unite_number": unite_number,
            "public_key": unit_public_key
        }
        init = False
        datas = json.dumps(datas).encode('utf-8')
    else:
        datenow = datetime.now()
        created_at = datenow.isoformat()
        stamp = datetime.timestamp(datenow)
        xor = int(stamp) ^ 10000
        proof = xor << 2
        datas = {
            "unite_number": unite_number,
            "created_at": created_at,
            "automats": [],
            "proof": proof,
        }
        for i in range(10):
            automat_type = automat_types[i]
            automat_number = i + 1
            tank_temp = round(random.random() * 1.5 + 2.5, 1)
            ext_temp = round(random.random() * 6 + 8, 1)
            milk_weight = round(random.random() * 1095) + 3512
            ph = round(random.random() * 0.4 + 6.8, 1)
            kplus = round(random.random() * 12) + 35
            nacl = round(random.random() * 0.7 + 1, 1)
            salmonella = round(random.random() * 20) + 17
            e_coli = round(random.random() * 14) + 35
            listeria = round(random.random() * 26) + 28
            automat_infos = {
                "automat_type": automat_type,
                "automat_number": automat_number,
                "tank_temp": tank_temp,
                "ext_temp": ext_temp,
                "milk_weight": milk_weight,
                "ph": ph,
                "kplus": kplus,
                "nacl": nacl,
                "salmonella": salmonella,
                "e_coli": e_coli,
                "listeria": listeria
            }
            datas['automats'].insert(i, automat_infos)
        # write json file in filesystem
        datas = json.dumps(datas).encode('utf-8')
        f = open('/jsonsavefiles/' + str(stamp) + '.json', 'wb')
        f.write(datas)
        f.close()
        # encrypt datas
        encrypt_datas = gpg.encrypt(datas, 'collector@mail.com')
        datas = encrypt_datas.data

    ClientMultiSocket = socket.socket()
    host = 'collector'
    port = 65432
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    res = ClientMultiSocket.recv(1024 * 8)
    ClientMultiSocket.send(datas)
    received = ClientMultiSocket.recv(1024 * 8)
    received = convert_data(received)
    if('public_key' in received):
        path_public_collector_key = '../.keys/collector.gpg'
        file_exists = exists(path_public_collector_key)
        if not file_exists:
            f = open('../.keys/collector.gpg', 'x')
            f.write(received['public_key'])
            f.close()
            f = open('../.keys/collector.gpg', 'r')
            import_result = gpg.import_keys(f.read())
            gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE')
            f.close()

    ClientMultiSocket.close()
    time.sleep(60)
