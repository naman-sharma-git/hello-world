"""
recursive fuctiion is a function that calls itself till a certain conditiuon not meet
factorial of n = n * (n - 1) * (n - 2) * ... * 2 * 1
n!
4 = 4 * 3 * 2 * 1 - 24
"""


def fact(num):
    factorial = 1

    while num > 1:
        factorial *= num
        num -= 1

    return factorial

num = int(input("enter the number: "))
print(f"factorial of {num} is {fact(num)}")


def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

    
34
