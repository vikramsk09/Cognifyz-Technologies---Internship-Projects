def email_validator(email):
    if "@" in  email and ".com" in email:
        print(f"'{email}' is a valid email.")
    else:
        print(f"'{email}' is not a valid email.")
    
email = input("Enter the email address: ")
email_validator(email)
