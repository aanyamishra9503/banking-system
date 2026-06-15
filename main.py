from auth import register, login, logout, change_password, is_logged_in, current_username
from transaction import deposit, withdraw, transfer
from reports import transaction_history, monthly_summary, generate_summary
from databasebank import cur,db
import auth

while True:
    if not auth.is_logged_in():
        print("\n--- Banking System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            register()
        elif ch == "2":
            login()
        elif ch == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

    else:
        print("1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Monthly Summary")
        print("7. Generate Statement")
        print("8. Change Password")
        print("9. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            cur.execute("SELECT balance FROM accounts WHERE account_id=%s", (auth.current_user,))
            balance = cur.fetchone()[0]
            print("Current balance: ₹", balance)

        elif ch == "2":
            deposit()
        elif ch == "3":
            withdraw()
        elif ch == "4":
            transfer()
        elif ch == "5":
            transaction_history()
        elif ch == "6":
            monthly_summary()
        elif ch == "7":
            generate_summary()
        elif ch == "8":
            change_password()
        elif ch == "9":
            logout()
        else:
            print("Invalid choice.")