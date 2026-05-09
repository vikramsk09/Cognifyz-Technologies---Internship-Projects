def password_strength_checker(password):

    if len(password) < 8:
        print("Password length must be at least 8 characters.")
        return

    if not any(char.isdigit() for char in password):
        print("Please include at least 1 digit.")
    elif not any(char.isupper() for char in password):
        print("Please include at least 1 uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Please include at least 1 lowercase letter.")
    elif not any(not char.isalnum() for char in password):
        print("Please include at least 1 special character.")
    else:
        print("Strong Password ✅")

password = input("Enter your Passwrod: ")
password_strength_checker(password)

