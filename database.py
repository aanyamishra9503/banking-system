#database tables to be added 
#table user 
#table accounts
#table transaction

import mysql.connector as sql

db = sql.connect(host="localhost",
                 user="root",
                 password="my25sqlroot2008",
                 database="banksystem")

cur = db.cursor()
cur.execute(""" CREATE DATABASE banksystem
""")
cur.execute("""CREATE TABLE IF NOT EXIST user""")
db.commit()
print("Database connected and tables ready.")