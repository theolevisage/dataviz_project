CREATE DATABASE IF NOT EXISTS datas;

USE datas;

CREATE TABLE IF NOT EXISTS automat (
    unite_number INT,
    created_at TIMESTAMP,
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
    PRIMARY KEY(unite_number, created_at, automat_number)
);

CREATE TABLE IF NOT EXISTS pub_key (
    unite_number INT,
    pub_key BLOB,
    ban TINYINT(1),
    PRIMARY KEY(unite_number)
);