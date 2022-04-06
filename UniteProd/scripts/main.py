import os
import socket
import json
import random
import time
from datetime import datetime

unite_number = os.getenv('UNITE_NUMBER')
automat_types = [13, 12, 15, 9, 8, 2, 6, 8, 5, 2]
time.sleep(10)
while True:
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
    ClientMultiSocket = socket.socket()
    host = 'collector'
    port = 65432
    print('Waiting for connection response')

    datas = json.dumps(datas).encode('utf-8')
    jsonObj = json.loads(datas)

    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    res = ClientMultiSocket.recv(1024 * 8)
    ClientMultiSocket.send(datas)
    received = ClientMultiSocket.recv(1024 * 8)
    ClientMultiSocket.close()
    time.sleep(60)
