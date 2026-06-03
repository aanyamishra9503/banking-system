CREATE DATABASE IF NOT EXISTS banking-system;
USE banking-system;

CREATE TABLE accounts(
    account-id INT AUTO_INCREMEMT PRIMARY KEY,
    fullname VARCHAR(25) NOT NULL,
    email VARCHAR(25) UNIQUE,
    phone INT UNIQUE,
    password VARCHAR(255) NOT NULL,
    balance DECIMAL (12,2) DEFAULT 0.00,
    created-at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);