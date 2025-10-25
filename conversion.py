Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #type conversion/ type coating
>>> num1 = 100
>>> 
>>> num1
100
>>> type(num1)
<class 'int'>
>>> 
>>> float(num1)
100.0
>>> 
>>> num2 = float(num)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    num2 = float(num)
NameError: name 'num' is not defined. Did you mean: 'num1'?
>>> num2 = float(num1)
>>> 
>>> num2
100.0
>>> 
>>> type(num2)
<class 'float'>
>>> 
>>> num1
100
>>> 
>>> type(num1)
<class 'int'>
>>> 
>>> num1 = float(num1)
>>> num1
100.0
>>> type(num1)
<class 'float'>
>>> 
