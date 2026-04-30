Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#len()
#count()
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count("l")
4
a.count(" ")
3
#find a string
a="code is a code even its a simple code"
a.fint
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.fint
AttributeError: 'str' object has no attribute 'fint'. Did you mean: 'find'?
da.find("c")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    da.find("c")
NameError: name 'da' is not defined. Did you mean: 'a'?
a.find("c")
0
a.find("code")
0
a.find("its")
20
#escape sequences
#/n --> new line
#/t --> tab space
a="name\nmobileno\temailid
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobileno\temailid"
a
'name\nmobileno\temailid'
a="name\n mobileno\t emailid"
a
'name\n mobileno\t emailid'
print(a)
name
 mobileno	 emailid
a="name\nmobileno\temailid"
print(a)
name
mobileno	emailid
a="name:Lokesh\nmobileno:8989889998\temailid:lokjij@ksjdbck
SyntaxError: unterminated string literal (detected at line 1)
a="name:Lokesh\nmobileno:8989889998\temailid:lokjij@ksjdbck
"
SyntaxError: unterminated string literal (detected at line 1)
a="name:Lokesh\nmobileno:8989889998\temailid:lokjij@ksjd"
print(a)
name:Lokesh
mobileno:8989889998	emailid:lokjij@ksjd
#replace
a="abcalijlfihfonvz xmnbeuefeiuwgifygqpqwdj"
a.replace("a","*")
'*bc*lijlfihfonvz xmnbeuefeiuwgifygqpqwdj'
a="lokesh"
a.upper()
'LOKESH'
a=a.upper()
a
'LOKESH'
a.lower()
'lokesh'
a.capitalize()
'Lokesh'
a="lokesh is learning a course at codegnan rn"
a.title()
'Lokesh Is Learning A Course At Codegnan Rn'
a.upper()
'LOKESH IS LEARNING A COURSE AT CODEGNAN RN'
a.lower()
'lokesh is learning a course at codegnan rn'
a
'lokesh is learning a course at codegnan rn'
a.capitalize()
'Lokesh is learning a course at codegnan rn'
a="data"
a.isupper()
False
a.islower()
True
a.isalpha()
True
a.isdigit()
False
b="python code"
b.isalpha() #it dosent consider special char as alphabet
False
c="pythoncourse"
c.isalpha()
True
a="loki123"
a.isdight()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.isdight()
AttributeError: 'str' object has no attribute 'isdight'. Did you mean: 'isdigit'?
a.isdigit()
False
a.isalnum()
True
b="45678"
b.isdigit()
True
b.isnumeric()
True
b="123@123"
b.isdigit()
False
b.isnumeric()
False
a="6/7"
a.isnumeric()
False
a.isdigit()
False
a.isdecimal()
False
a=7.8
a.isdecimal()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.isdecimal()
AttributeError: 'float' object has no attribute 'isdecimal'
a="7.8"
a.isdecimal()
False
b="9"
b.isdecimal()
True
a="lokesh"
b="gupta"
print(a,b)
lokesh gupta
print(a+b)
lokeshgupta
print(a+" "+b)
lokesh gupta
print((a+" "+b).title())
Lokesh Gupta
#strip
#lstrip
#rstrip
a="       Lokesh        "
a
'       Lokesh        '
a.strip()
'Lokesh'
a.lstrip()
'Lokesh        '
a.rstrip()
'       Lokesh'
a=a.replace(" ","*")
a
'*******Lokesh********'
a.strip("*")
'Lokesh'
a.lstrip('*')
'Lokesh********'
a.rstrip('*')
'*******Lokesh'
a.split()
['*******Lokesh********']
a="lokesh is learning and improving himself daily"
a.split()
['lokesh', 'is', 'learning', 'and', 'improving', 'himself', 'daily']
a.split('l')
['', 'okesh is ', 'earning and improving himse', 'f dai', 'y']
#join
a=a.split()
a
['lokesh', 'is', 'learning', 'and', 'improving', 'himself', 'daily']
"".join()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    "".join()
TypeError: str.join() takes exactly one argument (0 given)
>>> "".join(a)
'lokeshislearningandimprovinghimselfdaily'
>>> " ".join(a)
'lokesh is learning and improving himself daily'
>>> "*".join()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    "*".join()
TypeError: str.join() takes exactly one argument (0 given)
>>> "*".join(a)
'lokesh*is*learning*and*improving*himself*daily'
>>> a=5
>>> b=8
>>> print(a+b)
13
>>> #formatting
>>> print("the ans is",a+b)
the ans is 13
>>> #format method
>>> a="motu"
>>> b="patlu"
>>> print("hello {} and {}.".format(a,b))
hello motu and patlu.
>>> print("hello {} hello{}".format(a,b))
hello motu hellopatlu
>>> #fstring
>>> print(f"hello {a} and {b}.")
hello motu and patlu.
>>> print(f"hello {a} hello {b}.")
hello motu hello patlu.
>>> f"hello {a} hello {b}."
'hello motu hello patlu.'
>>> a,b=40,33
>>> f'multiplying {a} and {b} gives {a*b}'
'multiplying 40 and 33 gives 1320'
>>> 'multiplying {} and {} gives {}'.format(a,b,a*b)
'multiplying 40 and 33 gives 1320'
>>> c=a*b
>>> f'multplying a and b gives {c}'
'multplying a and b gives 1320'
>>> 'multiplying a and b gives {}'.format(c)
'multiplying a and b gives 1320'
