from calendar import month

from auth import logged_or_not,current_user
from databasebank import cur, db
import csv
def transaction_history():
    if not logged_or_not():
        print("login first.")
        return
    cur.execute("SELECT * FROM transactions WHERE account_id=%s",(current_user),)
    show_all= cur.fetchall()
    if not show_all:
        print("No transactions found.")
        return
    for i in show_all:
        print(i)

def monthly_summary():
    if not logged_or_not():
        print("login first.")
        return
    month = input("Enter month (1-12): ").strip()
    year = input("Enter year (e.g. 2025): ").strip()

    if not month.isdigit() or not year.isdigit(): #txn_date= 2026-06-15 10:30:00
        print("Invalid input!")
        return
    cur.execute("SELECT * FROM transactions WHERE MONTH(transaction_date)= %s AND YEAR (transaction_date)= %s AND account_id=%s",(month,year,current_user)) 
    rows= cur.fetchall()
    if not rows:
        print("No transactions found for the specified month and year.")
        return
    for r in rows:
        print(r)

    cur.execute("""SELECT SUM(amount) FROM transactions WHERE transaction_type='deposit' AND MONTH(transaction_date)= %s AND YEAR(transaction_date)= %s AND account_id=%s""",(month,year,current_user,))
    total_deposits= cur.fetchone()[0] or 0

    cur.execute("""SELECT SUM(amount) FROM transactions WHERE transaction_type= 'withdraw' AND MONTH(transaction_date)= %s AND YEAR(transaction_date)= %s AND account_id=%s""",(month,year,current_user,))
    total_withdrawals= cur.fetchone()[0] or 0
    print("\nTotal Deposited:", total_deposits)
    print("Total Withdrawn:", total_withdrawals)

def generate_summary():
    if not logged_or_not():
        print("login first.")
        return
    cur.execute("SELECT * FROM transactions WHERE account_id=%s",(current_user,))
    rows= cur.fetchall()
    headers=["Transaction ID", "Account_id", "Transaction Type", "Amount", "Balance After", "Description", "Transaction Date"]
    with open("summary.txt","w", newline="") as f:
        writer=csv.writer(f, delimiter="\t")
        writer.writerow(headers)
        writer.writerows(rows)
    print("Summary generated successfully as summary.txt")
