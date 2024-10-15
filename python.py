#gussing game

import random
target = random.randint(1,100)
guess = 0
attempt = 0

while guess != target:
    guess = int(input("Enter a number between 1 to 100:"))
    attempt += 1

    if guess > 100 or guess < 0:
        print("Invalid input, enter no. between 1 to 100")
    elif guess > target:
        print("Try with lower number")
    elif guess < target:
        print("Try with larger number")
    else:
        print("You Guessed Correctly")
        print("Total Attempt Taken:", attempt)
        break
