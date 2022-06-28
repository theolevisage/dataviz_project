import json
import os


def get_automats_types():
    types = []
    for i in range(10):
        types.insert(i, os.getenv('AUTOMAT_' + str(i + 1) + '_TYPE'))
    return types


def convert_data(binary_data):
    str_data = binary_data.decode("UTF-8")
    try:
        data = json.loads(str_data)
    except:
        data = str_data
    finally:
        return data


def get_last_sequence_number():
    if os.path.isfile('/lastsequencenumber/number.txt'):
        f = open('/lastsequencenumber/number.txt')
        new_sequence_number = int(f.readline()) + 1
        f.close()
    else:
        new_sequence_number = 1
    return new_sequence_number
