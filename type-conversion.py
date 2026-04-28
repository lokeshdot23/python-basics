Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data type conversions
#int
int(8)
8
int(9.0)
9
int("str")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("str")
ValueError: invalid literal for int() with base 10: 'str'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
floar(6)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    floar(6)
NameError: name 'floar' is not defined. Did you mean: 'float'?
float(6)
6.0
float(3.8)
3.8
float('str')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float('str')
ValueError: could not convert string to float: 'str'
float(4+9j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(4+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#string
str(8)
'8'
str(4.5)
'4.5'
>>> str('str')
'str'
>>> str(6+9j)
'(6+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> str(name)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    str(name)
NameError: name 'name' is not defined
>>> complex(34)
(34+0j)
>>> complex(3.4)
(3.4+0j)
>>> complex('str')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex('str')
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(234)
True
>>> bool(3.3)
True
>>> bool('str')
True
>>> bool(6+6j)
True
>>> bool(True)
True
>>> bool(False)
False
