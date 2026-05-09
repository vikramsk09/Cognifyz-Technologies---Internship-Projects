import random

num = random.randint(1, 100)
print(f"Computer selected a number from 1-100, now it's your turn.")

turns = 0
while True:
    try:
        guess = int(input("Enter the guessed number = "))
        if guess == num:
            print("You got it right!")
            break
        elif guess < num:
            print("\tToo low.")
            turns += 1
        elif guess > num:
            print("\tToo high.")
            turns += 1
    except:
        print("Wrong input. Please try again.")
        continue

print("\nNumber of turns =", turns+1, "\n")
