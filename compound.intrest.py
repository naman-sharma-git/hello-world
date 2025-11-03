Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... amount = float(input = p(1 + r/100) ** t
... ci = amount  - p
... """
... principal = float(input("enter principal amount: "))
... rate = float(input("enter interest rate: "))
... time = float(input("enter time: "))
... #amount1 = principal * (1 + rate/100) ** time
... amount2 = principal * pow((1 + rate/100), time)
... print(round(amount2, 2))
... ci = amount2 - principal
