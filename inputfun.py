Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = "mark"
name
'mark'
first_name = input()
jhon
john
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    john
NameError: name 'john' is not defined
print(first_name)
jhon

age = input()
65
print(age)
65

first_name = input("enter your name")
enter your namejill

print(first_name)
jill

age = input("how old are you? ")
how old are you? 30

print(age)
30

num1 = input("enter a number: ")
enter a number: 23
num2 = input("enter another number: ")
enter another number: 12
print(num1)
23
print(num2)
12

result = num1 + num2
>>> print(result)
2312
>>> tpe(num1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tpe(num1)
NameError: name 'tpe' is not defined. Did you mean: 'type'?
>>> type(num1)
<class 'str'>
>>> type(num2)
<class 'str'>
>>> 
>>> num1 = int(num1)
>>> int(num1)
23
>>> int(num2)
12
>>> result = int(num1) + int(num2)
>>> print(result)
35
>>> 
>>> year = input("what is a current year: ")
what is a current year: 2025
>>> age = input("what is your age? ")
what is your age? 43
>>> 
>>> #your were born in the year 1982
>>> 
>>> int(year) - int(age)
1982
>>> 
>>> born_year = int(year) - int(age)
>>> print(your are born in born_year)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("your are born in the year", born_year)
your are born in the year 1982
>>> 
