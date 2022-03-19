CREATE DATABASE IF NOT EXISTS datas;

USE datas;

CREATE TABLE IF NOT EXISTS automats (
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

/* test values */
INSERT INTO automats VALUES (1, current_timestamp(), 1, 1, 0.1, 0.1, 1, 0.1, 1, 0.1, 1, 1, 1);
INSERT INTO automats VALUES (2, current_timestamp(), 1, 1, 0.1, 0.1, 1, 0.1, 1, 0.1, 1, 1, 1);
INSERT INTO automats VALUES (3, current_timestamp(), 1, 1, 0.1, 0.1, 1, 0.1, 1, 0.1, 1, 1, 1);