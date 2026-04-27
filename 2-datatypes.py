Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=6
>>> type(a)
<class 'int'>
>>> b=1.222222
>>> typr(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    typr(b)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> type(b)
<class 'float'>
>>> c='code'
>>> d="django"
>>> e="python"
>>> type(c)
<class 'str'>
>>> x=7+9k
SyntaxError: invalid decimal literal
>>> x=7+9j
>>> type(x)
<class 'complex'>
>>> y=9j
>>> typr(y)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    typr(y)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> type(y)
<class 'complex'>
>>> d=8+6i
SyntaxError: invalid decimal literal
>>> a=True
>>> type(a)
<class 'bool'>
>>> d=true
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> d=True
