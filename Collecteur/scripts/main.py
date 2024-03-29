import socket
from _thread import *
import time
import json
import gnupg

from config import proof_config, host, port
from datetime import datetime
from db import connect_to_db, insert_anomalies, insert_automats_data, insert_production_unit, is_banned, toggle_ban, insert_log, get_errors_number, update_error_number
from utils import get_errors_data, check_proof, convert_data

gpg = gnupg.GPG('/usr/bin/gpg')
gpg.encoding = 'utf-8'

time.sleep(10)

ServerSideSocket = socket.socket()
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
        data = connection.recv(2048 * 4)
        if data:
            dict_data = convert_data(data)
            key = "public_key"
            if key in dict_data:
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
                        errors = get_errors_data(dict_data)
                        nb_errors = len(errors)
                        if nb_errors == 0:
                            data_inserted = insert_automats_data(dict_data)
                        else:
                            data_inserted = insert_anomalies(dict_data)
                            level = 'error'
                            message = 'Entries has been saved in anomalies table due to some error. Unit number : ' + unit_number
                            insert_log(datetime.now(), message, level)
                            print(message)
                            update_error_number(unit_number, nb_errors)
                            total_nb_errors = get_errors_number(unit_number)
                            print('total error : ' + str(total_nb_errors))
                            if total_nb_errors > 3:
                                toggle_ban(unit_number, 1)
                                level = 'fatal'
                                message = 'Unit ' + unit_number + ' has been banned because of too many wrong values'
                                insert_log(datetime.now(), message, level)
                                print(message)
                    else:
                        print('proof does not match, do not insert datas')
                else:
                    print(str(dict_data['unit_number']), 'is banned')
                    # this machine is banned, special treatment ?
                payload = {
                    "name": "collector",
                    "data_inserted": data_inserted,
                    "sequence_number": dict_data['sequence_number']
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
