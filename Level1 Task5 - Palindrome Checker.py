text = input("Enter the text to check whether it is a Palindrome: ").lower().strip().replace(" ", "")

if text == text[::-1]:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")

