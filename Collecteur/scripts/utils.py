from datetime import datetime
import json
from config import proof_config


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
        print("errors")
        print(errors)
        print(len(errors))
    return len(errors) == 0


def check_proof(sended_proof, created_at, unit_nb):
    decalage = proof_config[unit_nb]["decalage"]
    exposant = proof_config[unit_nb]["exposant"]
    datetime_created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
    stamp = datetime.timestamp(datetime_created_at)
    xor = int(stamp) ^ exposant
    needed_proof = xor << decalage
    return sended_proof == needed_proof


def convert_data(binary_data):
    str_data = binary_data.decode("UTF-8")
    try:
        data = json.loads(str_data)
    except:
        data = str_data
    finally:
        return data