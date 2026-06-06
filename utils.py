def validate_amount(amount):
    try:
        amt = float(amount)      # converts "500" → 500.0
        if amt <= 0:
            print("Amount must be greater than 0!")
            return False
        return True
    except ValueError:
        print("Invalid amount!")
        return False

def format_currency(amount):
    print(f"₹ {float(amount):,.2f}")

def validate_phone(phone):
        if not phone.isdigit() or len(phone) != 10:
            print("invalid phone number.")

def validate_email(email):
    emailcheck= email.split("@")
    if len(emailcheck) !=2:
        print("invalid , please try again.")
        return False
    if "." not in emailcheck[1]:
         print("invalid ,please try again.")
         return False
    return True

   
    
