Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = 'jhon'
print(name)
jhon

age = 28
print(age)
28

print(name ' age)
      
SyntaxError: unterminated string literal (detected at line 1)
print(name ' age)
      
SyntaxError: unterminated string literal (detected at line 1)
print(name ' age)
      
SyntaxError: unterminated string literal (detected at line 1)

print(name, age)
      
jhon 28

print(10, 33,21,13)
      
10 33 21 13

print(10,21,33,30, sep=" ")
      
10 21 33 30

print(10,20,30,40, sep="#")
      
10#20#30#40

print(10,20,30,40, sep='hi')
      
10hi20hi30hi40

print("python")
      
python


num1 = 100
      
num2 = 200
      
result = num1 + num2
      
print(num1 , num2 , result)
      
100 200 300

#addition of 100 and 200 is 300
      

print("addition of", num1, "and", num2, "is", result)
      
addition of 100 and 200 is 300

name
      
'jhon'
>>> age
...       
28
>>> prinnt(name,age)
...       
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    prinnt(name,age)
NameError: name 'prinnt' is not defined. Did you mean: 'print'?
>>> print(name,age)
...       
jhon 28
>>> 
>>> # name: jhon, #age: 28
...       
>>> print("name:", name, "age:", age)
...       
name: jhon age: 28
>>> 
>>> 
>>> day=9
...       
>>> year=2007
...       
>>> months=2007
...       
>>> print("day", 'months' 'year' sep="/")
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("day", "months" "year" sep="/")
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(day, months, year sep='/')
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(day, months, year, sep='/')
...       
9/2007/2007
