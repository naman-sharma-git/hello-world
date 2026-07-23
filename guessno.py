"""
Create a simple number guessing game.
the user have 10 chance to guess the number.
if the user guess the number before 10 , stop asking about the number,  say CONGRATS and end the game
if user never guess the number , ask 10 times and end the game !!!
"""

import random

num = 1
print("welcome to the number guessing game., we have a number which need to be guessed , you have 10 attempts")
print("the secret number is between 1 to 50")

secret_number = random.randint(1 , 50)

attempts = 10

while num <= 10:
    print(f"you have {attempts} attemps left!!")
    user_number = int(input("guess the number:"))

    if user_number == secret_number:
        print("congrets..!! , you guess the write number")
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "try higher"
        else:
            higher_or_lower = "try lower"
        print(f"your guess is wrong , Try {higher_or_lower} number ")

    num += 1
    attempts -= 1

print(f" THE SECRET NUMBER WAS {secret_number}, GAME OVER !!!")

