Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#integers

age = 25
age
25


type(age)
<class 'int'>


#floats

present = 88.6
present
88.6


type(present)
<class 'float'>

10 + 33
43

7 + 3.4
10.4

#strings

name = "allen"


name
'allen'

type(name)
<class 'str'>


#boolean

#True and False

val = True
val
True

type(val)
<class 'bool'>

val2 = False
val2
False

type(val2)
<class 'bool'>


#none

#None
val4 = None
val4
val4

#None
val3 = None
val3


type(val3)
<class 'NoneType'>


s1 = "hello world"
s1
'hello world'

type)(s1)
SyntaxError: unmatched ')'
type(s1)
<class 'str'>

s2 = 'we are learnig python'
s2
'we are learnig python'


s3 = """hello world.
we are looking at strings.
bye"""
s3
'hello world.\nwe are looking at strings.\nbye'


s4 = "python"

len(s4)
6

s5 = "naman sharma"
s5
'naman sharma'
len(S5)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    len(S5)
NameError: name 'S5' is not defined. Did you mean: 's5'?
s5 = "naman sharma"
len(s5)
12


s5[3]
'a'

s3[2]
'l'


s3[9]
'l'

s5[m]
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s5[m]
NameError: name 'm' is not defined


s8 = "we are learning python"
len(-1)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    len(-1)
TypeError: object of type 'int' has no len()
>>> s8 = "we are learning python"
>>> s8
'we are learning python'
>>> len(-1)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    len(-1)
TypeError: object of type 'int' has no len()
>>> 
>>> 
>>> s8 = "we are learning python"
... s8
... 'we are learning python'
SyntaxError: multiple statements found while compiling a single statement
>>> s8 = "we are learning python"
>>> s8
'we are learning python'
>>> s8[-1]
'n'
>>> 
>>> 
>>> s1 = "hello world"
>>> s2 = "my self naman"
>>> 
>>> s1 = "hello world"
>>> s1
'hello world'
>>> s2 = "my self naman"
>>> s2
'my self naman'
>>> 
>>> s1 +
SyntaxError: invalid syntax
>>> s1 + s2
'hello worldmy self naman'
>>> s1 + ' ' + s2
'hello world my self naman'
