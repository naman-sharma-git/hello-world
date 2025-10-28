Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
str(100)
'100'

str(10.33)
'10.33'


int('12343')
12343

float('78.34)
      
SyntaxError: unterminated string literal (detected at line 1)
float('78.34')
      
78.34
vall = True
      
vall
      
True

type(vall)
      
<class 'bool'>

str(vall)
      
'True'

bool('python')
      
True

bool(100)
      
True

bool(1.4)
      
True

bool(0)
      
False

bool(0.0)
      
False

bool(103)
      
True

bool(-123)
      
True

bool(0.4)
      
True

bool("hi")
      
True

bool(' ')
      
True

#empty string => '', "", '''''',""""""
      
bool(""0
     
SyntaxError: '(' was never closed

bool("")
     
False

#None
     

bool(None)
     
False


int(200)
     
200
int(true)
     
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> int(200)
...      
200
>>> 
>>> int(True)
...      
1
>>> 
>>> int(False)
...      
0
>>> 
>>> 
>>> float(true)
...      
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    float(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> float(True)
...      
1.0
>>> 
>>> float(False)
...      
0.0
>>> 
>>> str(flase)
...      
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    str(flase)
NameError: name 'flase' is not defined
>>> str(False)
...      
'False'
>>> 
>>> str(None)
...      
'None'
