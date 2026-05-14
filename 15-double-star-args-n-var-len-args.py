#variable length args
'''
def check(*a):
    print(a)
    print(type(a))
check()# prints empty () and type is tuple
check(2,3,4,5)#prints 2,3,4,5 in tuple and type is tuple
b=[1,2,3,4,5]
check(*b)#here * spreads b list elements and passed through the check function
c={2,3,4,5,5}
check(*c)
d={'name':'lokesh','city':'vja'}
check(*d)#*d spreads only key values and prints keys and type tuple
#-----------------------------
def check1(*a):
    b=2
    print(a)
    print(type(a))
    for i in a:
        b=b+i
        print(b)
check1()
check1(2,3,4,5,6,7)
check1(1,2,3,4,5.2,4.3)
check1(2,3,4,5,"lokesh")
'''
#================================
#task only to add numbers ad floats and do not add strings or other typer
'''
def check1(*a):
    b=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) is (int or float or complex):
            b=b+i
            print(b)
check1(2,3,4,5+6j,'str')

def check1(*a):
    b=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            b=b+i
            print(b)
check1(2,3,4,5+6j,'str',True)
'''
#---------------------------------
#keyword variable length args
#kwargs(**)
'''
def Details(**a):
    print(a)
    print(type(a))
Details()
d={"idno":[10,20,30],"names":["lokesh","pranu","chinnu"],"status":["P","A","P"]}
Details(**d)

def Details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)#prints keywords
    for i in a.keys():
        print(i)#same keys
    for i in a:
        print(a[i])#prints values
    for i in a.values():
        print(i)#here we are directly getting values
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
        
d={"idno":[10,20,30],"names":["lokesh","pranu","chinnu"],"status":["P","A","P"]}
Details(**d)
'''
'''
#both * and ** usage
def final(*a,**b):
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    d=1
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
    print("keys values")
    for i,j in b.items():
        print(i,j)
final()
data=1,2,3.2,4.5,"str",6+9j,True,False
final(*data)
details={"idno":[10,20,30],"names":["lokesh","pranu","chinnu"],"status":["P","A","P"]}
final(**details)
final(*data,**details)
'''
#Task
#marks analysis report
'''
student count
ask each marks
s1 ?90
s2 59
s3 95
s4 96
s5 99
print total no of students
total marks of class
highest -99
lowest - 59
avg total//no of studs
'''
n=int(input("enter no of students: "))
list=[]
for i in range(n):
    print("enter marks of student no",i+1)
    list.append(int(input()))
print("class report:")
print("total no of students:",n)
print("total marks obtained by the class:",sum(list))
print("highest mark in class:",max(list))
print("lowest mark in class:",min(list))
print("average marks of the class:",(sum(list)/n))
