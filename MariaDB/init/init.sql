CREATE DATABASE IF NOT EXISTS datas;

USE datas;

CREATE TABLE IF NOT EXISTS production_unit (
    unit_number INT,
    ban TINYINT(1),
    PRIMARY KEY(unit_number)
);

CREATE TABLE IF NOT EXISTS automat (
    unit_number INT,
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
    PRIMARY KEY(unit_number, created_at, automat_number),
    CONSTRAINT FK_UnitNumber FOREIGN KEY (unit_number) REFERENCES production_unit(unit_number) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS anomaly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    occurence_date TIMESTAMP,
    unit_number INT,
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
    listeria INT
);