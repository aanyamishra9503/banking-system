import mysql.connector as sql

db= sql.connect(host="localhost", user="root", password="my25sqlroot2008", database="society")
cur= db.cursor()

cur.execute("""CREATE DATABASE IF NOT EXISTS bankingsystem;""")

cur.execute("""USE bankingsystem;""")
cur.execute("""
CREATE TABLE accounts(
    account-id INT AUTO_INCREMEMT PRIMARY KEY,
    fullname VARCHAR(25) NOT NULL,
    email VARCHAR(25) UNIQUE,
    phone INT UNIQUE,
    passkey VARCHAR(255) NOT NULL,
    balance DECIMAL (12,2) DEFAULT 0.00,
    created-at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
""")
cur.execute("""
CREATE TABLE transactions (
   transaction_id INT PRIMARY KEY AUTO_INCREMENT,
   account_no INT,
   transaction_type VARCHAR(20),   
   amount FLOAT,
   transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
   FOREIGN KEY (account_no)
   REFERENCES accounts(account_no));
""")
db.commit()
print("Database connected and tables ready.")