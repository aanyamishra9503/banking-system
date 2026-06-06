from utils import validate_amount, format_currency
from auth import logged_or_not, current_user
from databasebank import cur,db
def deposit():
    if not logged_or_not():
        print("please login first.")
        return
    enteramount= input("enter amount to be deposited: ").strip()
    if not validate_amount(enteramount):
        return
    enteramount= float(enteramount)
    cur.execute("UPDATE accounts SET balance + %s WHERE account_id=%s",(enteramount,current_user))
    cur.execute("SELECT balance FROM accounts WHERE account_id=%s",(current_user))
    new_balance= cur.fetchone()[0]
    #now log the transaction
    cur.execute("""INSERT INTO transactions(account_id, txn_type,amount, balance_after,description)VALUES(%s,%s,%s,%s,%s)""",(current_user, "deposit", enteramount, new_balance, "Deposit"))

    db.commit()
    print("amount deposited successfully.")
    format_currency(new_balance)





