from auth import logged_or_not,current_user
from databasebank import cur, db
def transaction_history():
    if not logged_or_not:
        print("login first.")
        return
    cur.execute("SELECT * FROM accounts WHERE account_id=%s",(current_user))
    show_all= cur.fetchall()
    for i in show_all:
        print(i)

    #how no transaction?

def monthly_summary():
    if not logged_or_not:
        print("login first.")
        return
    month= input("Enter month you want the details of: ")
    if not month.isalpha():
        print("Invalid choice entered.")
        return
    cur.execute("SELECT * FROM transactions WHERE transaction_date= %s AND account_id=%s",(month,current_user)) #its faulty, but how do i show month in my table
    cur.execute("""UPDATE accounts SET """)
