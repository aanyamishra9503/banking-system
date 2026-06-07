from utils import validate_amount, format_currency
from auth import logged_or_not, current_user
from databasebank import cur,db
minimum_balance= 500
def deposit():
    if not logged_or_not():
        print("please login first.")
        return
    enteramount= input("enter amount to be deposited: ").strip()
    if not validate_amount(enteramount):
        return
    enteramount= float(enteramount)
    cur.execute("UPDATE accounts SET balance + %s WHERE account_id=%s",(enteramount,current_user))
    cur.execute("SELECT balance FROM accounts WHERE account_id=%s",(current_user,))
    new_balance= cur.fetchone()[0]
    #now log the transaction
    
    cur.execute("""INSERT INTO transactions(account_id, txn_type,amount, balance_after,description)VALUES(%s,%s,%s,%s,%s)""",(current_user, "deposit", enteramount, new_balance, "Deposit"))

    db.commit()
    print("amount deposited successfully.")
    format_currency(new_balance)

def withdraw():
    if not logged_or_not:
        print("please login first.")
        return
    enterwithdraw_amount=input("enter amount to be withdrawn: ").strip()
    if not validate_amount(enterwithdraw_amount):
        return
    enterwithdraw_amount= float(enterwithdraw_amount)
    cur.execute("SELECT balance FROM accounts WHERE account_id= %s",(current_user,))
    cur_balance= cur.fetchone()[0]
    print("current balance: ",cur_balance)
    if cur_balance < enterwithdraw_amount:   
        print("insufficient balance ,can't withdraw money.")
        return
    if  cur_balance - enterwithdraw_amount < minimum_balance:
        print("Cannot withdraw! Minimum balance of ₹500 must be maintained.")
        return

    cur.execute("UPDATE accounts SET balance= balance- %s WHERE account_id=%s",(enterwithdraw_amount,current_user))
    db.commit()
    cur.execute("SELECT balance FROM accounts WHERE account_id=%s",(current_user,))
    new_balance= cur.fetchone()[0]
    cur.execute("""INSERT INTO transactions(account_id, txn_type,amount, balance_after,description)VALUES(%s,%s,%s,%s,%s)""",(current_user, "withdraw", enterwithdraw_amount, new_balance, "withdrawal"))

    db.commit()
    print("Amount withdrawn successfully.")
    format_currency(new_balance)
def transfer():
    if not logged_or_not():
        print("please login first.")
        return
    receiver_id = input("Enter receiver's account ID: ").strip()
    if not receiver_id.isdigit():          
        print("Invalid account ID!")
        return
    receiver_id = int(receiver_id) 
    cur.execute("SELECT account_id FROM accounts WHERE account_id = %s", (receiver_id,))
    if not cur.fetchone():       
        print("Receiver account does not exist!")
        return
    
    if receiver_id == current_user:
        print("Cannot transfer to your own account!")
        return
    
    send_amount= input("enter amout to be sent: ").strip()
    if not validate_amount(send_amount):
        return
    send_amount=float(send_amount)

    cur.execute("SELECT balance FROM accounts WHERE account_id=%s",(current_user,))
    cur_balance= cur.fetchone()[0]
    if cur_balance < send_amount:
        print("Insufficient balance, can't transfer money.")
        return

    if cur_balance - send_amount < minimum_balance:
        print("Minimum balance of ₹500 must be maintained!")
        return
    try:
        cur.execute("UPDATE accounts SET balance= balance - %s WHERE account_id=%s",(send_amount,current_user))
        cur.execute("UPDATE accounts SET balance=balance + %s WHERE account_id=%s",(send_amount,receiver_id))
        cur.execute("SELECT balance FROM accounts WHERE account_id=%s",(current_user,))
        sender_new_balance = cur.fetchone()[0]
        cur.execute("SELECT balance FROM accounts WHERE account_id=%s",(receiver_id,))
        receiver_new_balance = cur.fetchone()[0]
        cur.execute("""INSERT INTO transactions (account_id, txn_type, amount, balance_after, description) VALUES (%s, %s, %s, %s, %s)""",(current_user, "transfer", send_amount, sender_new_balance, f"Transfer to account {receiver_id}"))
        cur.execute("""INSERT INTO transactions (account_id, txn_type, amount, balance_after, description) VALUES (%s, %s, %s, %s, %s)""",
            (receiver_id, "transfer", send_amount, receiver_new_balance, f"Transfer from account {current_user}"))
        db.commit()
        print("transaction successful.")
        new_balance= format_currency(sender_new_balance)
        print("New balance: ",new_balance)

    except Exception as e:
        db.rollback()       #undoes everything if anything goes wrong
        print("Transfer failed! Please try again.")








