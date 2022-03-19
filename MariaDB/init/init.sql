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

INSERT INTO automats VALUES (1, 1646659067, 1, 1, 0.1, 0.1, 1, 0.1, 1, 0.1, 1, 1, 1);
INSERT INTO automats VALUES (1, 1646745467, 1, 1, 0.1, 0.1, 1, 0.1, 1, 0.1, 1, 1, 1);
INSERT INTO automats VALUES (1, 1646831867, 1, 1, 0.1, 0.1, 1, 0.1, 1, 0.1, 1, 1, 1);