CREATE DATABASE IF NOT EXISTS datas;

USE datas;

CREATE TABLE IF NOT EXISTS production_unit (
    unit_number INT,
    ban TINYINT(1),
    errors_count INT DEFAULT 0,
    PRIMARY KEY(unit_number)
);

CREATE TABLE IF NOT EXISTS automat (
    unit_number INT,
    created_at TIMESTAMP,
    sequence_number INT,
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
    PRIMARY KEY(unit_number, sequence_number, automat_number),
    CONSTRAINT FK_UnitNumber FOREIGN KEY (unit_number) REFERENCES production_unit(unit_number) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS anomaly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    occurence_date TIMESTAMP,
    unit_number INT,
    created_at TIMESTAMP,
    sequence_number INT,
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

CREATE TABLE IF NOT EXISTS log (
    created_at TIMESTAMP,
    message TEXT,
    level VARCHAR(10)
);