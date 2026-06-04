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

CREATE TABLE transactions (
   transaction_id INT PRIMARY KEY AUTO_INCREMENT,
   account_no INT,
   transaction_type VARCHAR(20),
   amount FLOAT,
   transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
   FOREIGN KEY (account_no)
   REFERENCES accounts(account_no)
);
