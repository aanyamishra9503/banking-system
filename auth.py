import hashlib
from datetime import datetime
from databasebank import db, cur
from utils import validate_phone, validate_email

current_user = None        # stores user_id after login
current_username = None    # stores username after login


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def logged_or_not():
    return current_user is not None

def register():
    username= input("Enter username: ").strip()
    if not username:
        print("username cannot be empty")
        return
    
    cur.execute("SELECT account_id FROM accounts WHERE username= %s",(username,))
    if cur.fetchone():
        print("username already taken, please try again.")
        return
    
    fullname= input("Enter full name: ").strip
    if not fullname:
        print("full name cannot be empty")
        return

    email= input("enter email id: ").strip()
    if not email:
        print("email cannot be empty")
        return
    cur.execute("SELECT account_id FROM accounts WHERE email=%s ",(email,))
    if cur.fetchone():
        print("email already registered, please try again.")
        return
    phone= int(input("enter your phone number: ")).strip()
    if not phone.isdigit() or len(phone)!=10:
        print("invalid phone number, must be 10 digits.")
        return
    password = input("enter your password: ").strip()
    if len(password)<8:
        print("password must be 8 characters long.")
        return
    hashed= hash_password(password)
    cur.execute("""INSERT INTO accounts (username, fullname,email,phone,passkey,balance) VALUES (%s,%s,%s,%s,%s,0.00)""",(username, fullname,email,phone,hashed))

    db.commit()

    #now show final recorded details
    cur.execute("SELECT account_id FROM accounts WHERE username= %s",(username,))
    account_id= cur.fetchone()[0]
    print("your account ID is: ", account_id)
    print("please login to continue.")

def login():
    global current_user, current_username
    username= input("enter your username: ").strip()
    password= input("enter you password: ").strip()
    hashed = hash_password(password)
    cur.execute("SELECT account_id, username FROM accounts WHERE username= %s AND passkey=%s",(username,hashed))
    user=cur.fetchone()


    if not user:
        print("invalid username or password, please try again.")
        return
    current_user= user[0]  #account_id
    current_username=user[1] #name

    print("Login successful, welcome ",current_username)
    print("your account ID: ", current_user)

def logout():
    global current_user, current_username
    if not logged_or_not():
        print("your are not logged in.")
        return
    print("goodbye ",current_username)

    current_user= None #clear session
    current_username= None 

def change_password():
    if not logged_or_not:
        print("please login first")
        return
    
    old_pass= input("enter your current password: ").strip()
    hashed_old= hash_password(old_pass)
    cur.execute("""SELECT account_id FROM accounts 
                WHERE account_id= %s AND passkey=%s""",(current_user,hashed_old))
    if not cur.fetchone():
        print("current password is incorrect.")
        return 
    
    new_pass= input("enter your new password, (password must contain 8 characters): ").strip()
    if len(new_pass)<8:
        print("password must be of 8 characters")
        return
    confirm= input("confirm password: ")
    if confirm !=new_pass:
        print("passwords do not match , try again")
        return
    hashed_new= hash_password(new_pass)
    cur.execute("""
        UPDATE accounts SET passkey = %s
        WHERE account_id = %s
    """, (hashed_new, current_user))
    db.commit()

    print("Password changed successfully!")