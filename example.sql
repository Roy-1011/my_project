CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE IF NOT EXISTS account (
    email VARCHAR(30) PRIMARY KEY,
    password VARCHAR(50) ,
);

INSERT INTO account (email, password) VALUES('12345@gmail.com', '54321wasd');

SELECT * FROM account;