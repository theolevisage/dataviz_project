CREATE DATABASE IF NOT EXISTS datas;

USE datas;

CREATE TABLE IF NOT EXISTS automats (
    unite_number INT,
    date TIMESTAMP,
    automat_type INT,
    automat_number INT,
    tank_temp FLOAT,
    ext_temp FLOAT,
    milk_weight INT,
    ph FLOAT,
    kplus INT,
    nacl FLOAT,
    salmonella INT,
    e_coli INT,
    listeria INT,
    PRIMARY KEY(unite_number, date, automat_number)
);
