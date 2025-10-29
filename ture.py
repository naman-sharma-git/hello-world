Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# comparison operators
# ==, !=, >, <, >=, <=

# ==

num1 = 100
num2 = 90
num3 = 90

num2 == num3
True

num1 == num2
False


'python' == 'Python'
False

'python' == 'python'
True

#!

num1 != num2
True

num2 != num3
False

# > - greater than

num1 > num2
True

num3 > num1
False

# < - less than

num1
100

num2
90
num3
90

num<num3
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    num<num3
NameError: name 'num' is not defined. Did you mean: 'num1'?
num1<num3
False

num3 < num1
True

# >=

num1 >= num2
True

num2 >= num3
True

num2 >= num1
False


# <=

num2 <= num1
True

num2 <= num3
True

num1 <= num2
False

num1 <= num2
False



# logical operators => and, or, not


# and

Ture and Ture
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    Ture and Ture
NameError: name 'Ture' is not defined

True and True
True

True and False
False
>>> 
>>> False and False
False
>>> 
>>> # or
>>> 
>>> True or True
True
>>> 
>>> True or False
True
>>> 
>>> False and True
False
>>> 
>>> 
>>> False or False
False
>>> 
>>> # not
>>> 
>>> not True
False
>>> 
>>> not False
True
>>> 
>>> name = 'makrs'
>>> age = 22
>>> 
>>> name == 'marks' and age >= 18
False
>>> 
>>> name = 'makrs'age = 22
SyntaxError: invalid syntax
>>> 
>>> name = 'marks'
>>> age =18
>>> 
>>> name == 'marks' and age >= 18
True
