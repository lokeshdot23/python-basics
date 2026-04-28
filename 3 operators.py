Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a//2)
1
print(a/2)
1.0
print(a*b)
8
print(a**b)
16
a%b
2
# above are arthematic
#Assignment operators
a=3
b=6
a+=b
a
9
a-=2
a
7
a*=4
a
28
a//=4
a
7
a/=2
a
3.5
a*=2
a
7.0
a**=2
a
49.0
a%=7
a
0.0
a=3
b=6
b+=a
b
9
b-=a
b
6
b//=3
b
2
b/=1
b
2.0
b*=9
b
18.0
b**=2
b
324.0
b%=9
b
0.0
#comparision
a=5
b=9
a<b
True
b>a
True
a<=b
True
b>=a
True
a>b
False
b<a
False
a>=b
False
b<=a
False
a!=b
True
a==b
False
#logical
a=6
b=3
a<b and b>a
False
a>b and a<b
False
a>b and b<a
True
a<=b and b>=a
False
a=5
b=9
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
not True
False
not False
True
not a>b
True
not a<b
False
not a>b or a<b
True
not a!=b or a==b
False
a>b or a<b
True
#identify
a=4
b=1.0
if a is int:
    print("its int")
else :
    print("its not int")

    
its not int
if a is int:
    print("int")

    
if type(a) is int:
    print("int")
else:
    print("not int")

    
int
if type(b) is int:
    print("int")
else:
    print("not int")

    
not int
if type(b) is not int:
    print("not int")

    
not int
if type(b) is float:
    print("float")
else:
    print("not float")

    
float
if type(a) is not int:
    print("int")

    
c="str"
if type(c) is str:
    print("str")

    
str
if type(c) is not str:
    print("sdf")

    
#membership
    
a=4,5,6,7,8,9,11,12
if 10 in a:
    print(10)

    
if 11 in a:
    print(11)

    
11
>>> if 15 in a:
...     print(15)
... 
...     
>>> if 15 not in a:
...     print(15)
... 
...     
15
>>> #bitwise
>>> a=4
>>> b=6
>>> bin(a)
'0b100'
>>> bin(b)
'0b110'
>>> a&b
4
>>> a|b
6
>>> ~5
-6
>>> a=8
>>> ~a
-9
>>> ''' a=5
... formulae -(x+1)
... '''
' a=5\nformulae -(x+1)\n'
>>> a=4
>>> b=6
>>> a^b
2
>>> ``` xor 00=0 11=0 10=1 01=1 '''
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> a,b=8,9
>>> a^b
1
>>> 5^10
15
>>> a=2
>>> a<<2
8
>>> #left shift adds 2 zeros to right side like 0010(2) ==> 001000(8)
>>> a=6
>>> a<<4
96
1>>2
0
a=5
a>>3
0
a=5
a>>2
1
#deletes right side 2 digits and adds zeros to left side
