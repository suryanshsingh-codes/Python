# 4. RANDOM NUMBER GUESSING GAME
print("4. RANDOM NUMBER GUESSING GAME")
print()

import random

secret = random.randint(1, 100)
print("Guess a number between 1 and 100")
print()


while True:
    guess = int(input("Enter your guess : "))
    print()

    print(f"Value of guess : {guess}")
    print(f"Secret Number : {secret}")
    print()

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {secret}")
    print()
    break
print()