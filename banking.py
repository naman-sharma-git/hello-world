def check_balance():
    print(f"your current balance is: {balance}")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("cannot withdraw negative and zero ammount ")
    elif amount > balance:
        print("cannot withdraw more the balance ammount")

    else:
        balance -= amount
        

        
def deposit(amount):
    
    global balance
    if amount >= 0:
        balance += amount

    else:
        print("cannot deposit negative amount")

  

balance = 0

print("welcome to ASI bank!!")

while True:
    print("1. check the balance")
    print("2. withdraw")
    print("3. deposit")
    print("4. Quit")
    choice = int(input("enter the your choice: "))

    if choice == 1:
        check_balance()

    elif choice == 2:
        amt = float(input("enter the amount to withdraw.."))
        withdraw(amt)

    elif choice == 3:
        amt = float(input("enter the amount to deposit.."))
        deposit(amt)

    elif choice == 4:
        break
    else: 
        print("invalid choice")

print("thankyou for banking with us!!")





