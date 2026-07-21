#role a dice

import random

print("welcome to the game of role the dice")

while True:
    choice = input("press 'enter' to role and press 'q' to quit")

    if choice == "q":
        print("thnnks for playing this game , byee..")
        break

    elif choice == '':
        number = random.randint(1 , 6)
        print(f"your nummber is {number}")

    else:
        print("invalid input")

