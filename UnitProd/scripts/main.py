import gnupg
import json
import os
import socket
import time
import utils

from datetime import datetime
from automat import Automat
from unit import Unit

init = True
gpg = gnupg.GPG('/usr/bin/gpg')
gpg.encoding = 'utf-8'
unit_number = os.getenv('UNIT_NUMBER')
name = os.getenv('NAME')
mail = os.getenv('MAIL')
decalage = os.getenv('DECALAGE')
exposant = os.getenv('EXPOSANT')

# create Automats
automats = []
automat_types = utils.get_automats_types()
for i in range(0, len(automat_types)):
    number = i+1
    automat_type = automat_types[i]
    automat = Automat(number, automat_type)
    automats.append(automat)

# create Unit
unit = Unit(name, mail, decalage, exposant, unit_number, automats)
time.sleep(10)


while True:
    if init:
        # keys
        unit_public_key = gpg.export_keys(name + ' <' + mail + '>')
        datas = {
            "unit_number": unit_number,
            "public_key": unit_public_key
        }
        datas = json.dumps(datas).encode('utf-8')
    else:
        datenow = datetime.now()
        stamp = datetime.timestamp(datenow)

        # generate a proof of work
        proof = unit.make_work_proof(stamp)
        created_at = datenow.isoformat()
        new_sequence_number = utils.get_last_sequence_number()

        # generate automats data
        datas = {
            "unit_number": unit.number,
            "sequence_number": new_sequence_number,
            "created_at": created_at,
            "automats": [],
            "proof": proof,
        }
        unit.generate_automats_data()
        print('avant hello')
        for automat in unit.automats:
            print('helloooooooooooooooooooooooooooooooooooooooo')
            datas['automats'].append(automat.infos)

        # write json file in filesystem
        datas = json.dumps(datas).encode('utf-8')
        f = open('/jsonsavefiles/' + str(new_sequence_number) + '.json', 'wb')
        f.write(datas)
        f.close()

        # write sequence number, w mode erase previous content
        f = open('/lastsequencenumber/number.txt', 'w')
        f.write(str(new_sequence_number))
        f.close()

        # encrypt datas
        encrypt_datas = gpg.encrypt(datas, 'collector@mail.com')
        datas = encrypt_datas.data

    # create socket client
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
    received = utils.convert_data(received)
    if 'public_key' in received:
        print('receiveeeeeeeeeeeeeeeeed')
        path_public_collector_key = '../.keys/collector.gpg'
        f = open(path_public_collector_key, 'w')
        f.write(received['public_key'])
        f.close()
        f = open(path_public_collector_key, 'r')
        import_result = gpg.import_keys(f.read())
        gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE')
        f.close()
        init = False
    else:
        decrypt_result = gpg.decrypt(received)
        if decrypt_result.ok:
            print(decrypt_result.data)
            new_sequence_number = utils.convert_data(decrypt_result.data)['sequence_number']
            os.remove('/jsonsavefiles/' + str(new_sequence_number) + '.json')

    ClientMultiSocket.close()
    time.sleep(60)
