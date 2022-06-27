import mysql.connector as mariadb
import gnupg
gpg = gnupg.GPG('/usr/bin/gpg')
gpg.encoding = 'utf-8'

def connect_to_db():
    return mariadb.connect(
        host="mariadb",
        port=3306,
        user="root",
        password="root123",
        database="datas")

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
                "INSERT INTO anomaly (occurence_date, unit_number, created_at, sequence_number, automat_type, automat_number, tank_temp, ext_temp, milk_weight, ph, kplus, nacl, salmonella, e_coli, listeria) VALUES (TIMESTAMP(%s), %s, TIMESTAMP(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (occurence_date, dict_data['unit_number'], datetime.fromisoformat(dict_data['created_at']), dict_data['sequence_number'], automat['automat_type'],
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
                "INSERT INTO automat (unit_number, created_at, sequence_number, automat_type, automat_number, tank_temp, ext_temp, milk_weight, ph, kplus, nacl, salmonella, e_coli, listeria) VALUES (%s, TIMESTAMP(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (dict_data['unit_number'], datetime.fromisoformat(dict_data['created_at']), dict_data['sequence_number'], automat['automat_type'],
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