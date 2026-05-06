#conditions
#if condition by using comparision operators
#<,>,<=,>=,!=,==
'''
a=4;b=8
if a<b:
    print("true")

a=4;b=8
if a>b:
    print("true")

a=4;b=8
if a<=b:
    print("true")

a=4;b=8
if a>=b:
    print("true")

a=4;b=8
if a!=b:
    print("not equal")

a=b=8
if a==b:
    print("equal")

a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")

a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("greater")

a=int(input("a value"))
b=7
if a>b:
    print("greater")

a="python"
if a!='java':
    print("not equal")

a='pyt'
if a=='pyt':
    print('equal')

a=input('data')
if a=='python':
    print("equal")
'''
#if else by using logical operators
#and or not
'''
a=7;b=9
if a<b and b>a:
    print('true')

a=7;b=9
if a<=b and b>=a:
    print('true')

a=5;b=10
if a!=b and b==a:
    print('true')

a=7;b=9
if a<b or b>a:
    print('true')

a=11;b=13
if a<=b or b>=a:
    print('true')

a=7;b=9
if a!=b or b==a:
    print('true')

a=7;b=9
if not a<b:
    print('less')

a=7;b=9
if not a>b:
    print('true')

a=7;b=9
if not a<b and b>a:
    print('less')

a=int(input('a value'))
b=int(input('b value'))
if a<b and b>a:
    print('less')

a=input("data")
if a=='loki' or a=='lokii':
    print("true")
'''
#is,is not
'''
a=6
if type(a) is int:
    print('int')

a=6
if type(a) is not int:
    print('int')

a=int(input("a val"))
if type(a) is int:
    print('int')

a=float(input('entre a float'))
if type(a) is float:
    print('float')

a=float(input('entre a float'))
if type(a) is not float:
    print('float')

a=(input('entre a str'))
if type(a) is str:
    print('str')

a=(input('entre a str'))
if type(a) is not str:
    print('str')
'''
#membership operators
'''
a=[20,30,40]
print(70 not in a)

a=[10,20,30,40,50,60]
if 60 in a:
    print('true')

a=[10,20,30,40,50,60]
if 60 not in a:
    print('true')

a=[10,20,30,40,50,60]
if 70 not in a:
    print('true')

a=int(input("enter a value"))
if 40 in a:
    print("40 present") # gives error single variable cannot use in or not in 

a=[2,3,4,5,6,7,8,9,10]
b=int(input('entre a val;'))
if b in a:
    print('present')

a=40
if 40 in a:
    print("40 present")#err

a=['c','pytho','java','mava','kava']
b='pytho'
if b in a:
    print("present")
'''
#if else conditions by using comparision operator
'''
a=3;b=6
if a<b:
    print("less")
else:
    print("greater")

a=3;b=6
if a>b:
    print("less")
else:
    print("greater")

a=3;b=6
if a<b and b>a:
    print("less")
else:
    print("greater")

a=3;b=6
if a<b and b<a:
    print("less")
else:
    print("greater")

a=3;b=6
if a<b or a>b:
    print("less")
else:
    print("greater")

a=3;b=6
if not a<b:
    print("less")
else:
    print("greater")

a=3;b=6
if type(a) is int:
    print("int")
else:
    print("not int")

a=3;b=6
if type(a) is not int:
    print("int")
else:
    print("not int")

a=[1,2,3,4,5,6,7,8,9]
if 2 in a:
    print("present")
else:
    print("not present")

a=[1,2,3,4,5,6,7,8,9]
if 12 in a:
    print("present")
else:
    print("not present")

a=[1,2,3,4,5,6,7,8,9]
if 2 not in a:
    print("present")
else:
    print("not present")
'''
