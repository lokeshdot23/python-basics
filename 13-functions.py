#functions
'''
a,b=10,20
print("sum of a b is",a+b)
print("diff of a b is",a-b)
print("mul of a b is ",a*b)
a,b=100,200
print("sum of a b is",a+b)
print("diff of a b is",a-b)
print("mul of a b is ",a*b)
a,b=1000,2000
print("sum of a b is",a+b)
print("diff of a b is",a-b)
print("mul of a b is ",a*b)
'''
'''
def calc(a,b):
    print("sum of a b is",a+b)
    print("diff of a b is",a-b)
    print("mul of a b is ",a*b)
calc(10,20)
calc(100,200)
calc(1000,2000)

def calc(a,b):
    print("pow od a b is", pow(a,2))
    print("mod of a,b is",a%b)
    print("int div od a b is",a//b)
calc(10,20)
calc(100,200)
calc(1000,2000)

def add(a,b):
    print(a+b)
add(2,3)

def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()

def fullname():
    a=input()
    b=input()
    print((a+" "+b).title())
fullname()

def course():
    print('python')
course()
'''
#print vs return
'''
def cal(a,b):
    c,d,e=a+b,a-b,a*b
    print(c)
    print(d)
    print(e)
cal(2,3)

def cal(a,b):
    c,d,e=a+b,a-b,a*b
    #return c
    #return d
    #return e
    return (c,d,e)
print(cal(3,5))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
while True:
    a=int(input('entre a val'))
    b=int(input('entre b val'))
    #print('type an option
    #            1. add
      #          2. sub
     #           3. mul')

    c=input()
    if c=='add':
        print(add(a,b))
    if c=='mul':
        print(mul(a,b))
    if c=='sub':
        print(sub(a,b))
#--------------------------------
def add(a,b):
    print( a+b)
def sub(a,b):
    print( a-b)
def mul(a,b):
    print( a*b)
a=int(input('entre a val'))
b=int(input('entre b val'))
print(''type an option
                1. add
                2. sub
                3. mul'')
c=input()
if c=='add':
    add(a,b)
if c=='mul':
    mul(a,b)
if c=='sub':
    sub(a,b)
'''
#--------------------------------
'''
while True:
    def calc():
        a=int(input('a'))
        b=int(input('b'))
        print('entre an option 1 add 2 sub 3 mul')
        c=int(input())
        if c==1:
            print(a+b)
        elif c==2:
            print(a-b)
        elif c==3:
            print(a*b)
        else:
            print('you entred a wrong no')
    calc()
'''
#---------------------------------
#split bill
'''
def split_bill():
    friends=int(input('frnds'))
    amount=int(input('bill'))
    print("per head-->",calc_each(friends,amount))
def calc_each(friends,amount):
    return amount//friends

split_bill()
'''
#----------------------------
'''
def split_bill():
    friends=int(input('frnds'))
    amount=int(input('bill'))
    print(f'per head --> {amount//friends}')
split_bill()
#---------------------------
def split_bill():
    friends=int(input('frnds'))
    amount=int(input('bill'))
    print('per head --> {}'.format(amount//friends))
split_bill()

def split_bill():
    friends=int(input('frnds'))
    amount=int(input('bill'))
    perhead=amount//friends
    print('per head --> {}'.format(perhead))
split_bill()
'''
#card ,account balance,pwd,enquiry, withdraw, deposit
'''
insert the card 'c'
welcome lokesh
entre the password 1234
options
1 balance enquiry
your acc balance is 1lakh rs
2 withdraw
amount entre
20000
remaininf balance 80000
else
invalid card
wrong pass

def atmfun():
    b=100000
    c=input("card").lower()
    if c=='card':
        print("welcome lokesh")
        p=input("pass").lower()
        if p=='1234':
            print("""options
        1. balance
        2. withdraw""")
            d=input()
            if d=='1':
                print("balance:",b)
            elif d=='2':
                amt=int(input("entre amt"))
                b=b-amt
                print("remaining:",b)
            else:
                print('invalid option')
        else:
            print("pass wrong")
    else:
        print("invalid card")
while True:
    atmfun()
'''
