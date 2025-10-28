Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#type conversion/ type casting
num1 = 100

num1
100

type(num1)
<class 'int'>

float(num1)
100.0

num2 = float(num1)

num2
100.0

type(num2)
<class 'float'>

num1
100

type(num1)
<class 'int'>

num1 = float(num1)
num1
100.0

type(num1)
<class 'float'>

num3 = 57.77

num3
57.77

int(num3)
57


int(78.85)
78

num1
100.0

num2
100.0
num3
57.77


num4 = 2000

num4
2000

str(num4)
'2000'


x = str(num4)

x
'2000'

type(x)
<class 'str'>


s1 = 'hello'

s1
'hello'


s2 = '3236342'

s2
'3236342'

type(s2)
<class 'str'>

int(s2)
3236342
>>> 
>>> y = int(s2)
>>> 
>>> y
3236342
>>> 
>>> type(y)
<class 'int'>
>>> 
>>> 
>>> s3 = '63.45'
>>> s3
'63.45'
>>> 
>>> float(s3)
63.45
>>> 
>>> s4 = 'python3.18'
>>> 
>>> s4
'python3.18'
>>> 
>>> language = "python"
>>> 
>>> version = 3.18
>>> 
>>> print(language + version)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print(language + version)
TypeError: can only concatenate str (not "float") to str
>>> 
>>> language + str(version)
'python3.18'
>>> 
>>> '100' + '100'
'100100'
>>> 
>>> int('100') + int('100')
200
>>> 
