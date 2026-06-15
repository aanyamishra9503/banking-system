import mysql.connector as sql
db = sql.connect(host="localhost", user="root", password="my25sqlroot2008R", database="banking")
cur= db.cursor()

cur.execute("""CREATE DATABASE IF NOT EXISTS bankingsystem;""")

cur.execute("""USE bankingsystem;""")
cur.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(25) NOT NULL,
    fullname VARCHAR(25) NOT NULL,
    email VARCHAR(50) UNIQUE,
    phone BIGINT UNIQUE,
    passkey VARCHAR(255) NOT NULL,
    balance DECIMAL (12,2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
""")
cur.execute("""
CREATE TABLE transactions (
   transaction_id INT PRIMARY KEY AUTO_INCREMENT,
   account_id INT,
   transaction_type VARCHAR(20),   
   amount DECIMAL(12,2),
   balance_after DECIMAL (12,2),
   description VARCHAR (100),
   transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY (account_id)
   REFERENCES accounts(account_id));
""")
# transaction type- deposit / withdraw / transfer
#balance after transaction

db.commit()
print("Database connected and tables ready.")