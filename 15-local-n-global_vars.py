#local and global var
#global var
'''
a=3
def check1():
    print("inside value is",a)
check1()
print("outside value is ",a)
#----------------------------------
a=3
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is ",a)
'''
#both global and local
'''
a=4;b=6
def check3():
    a=5
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12
    b=b+a
    print("value of b is:",b)
check3()
print("a value is ",a)
print("b val is",b)

#global keyword
a=5
def final():
    global a,b
    print("inside value is ",a)
    a=10
    print("updated value is ",a)
    #global b
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a val is ",a)
print("b val is ",b)
'''
