#key word and positional args
'''
def details(id,name,mailid):
    id=10
    name='lokesh'
    mailid='lok@gmail.com'
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
#============================================
def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=10,name="Lokesh",mailid="l@gmail.com")
details(id=20,name="pranu",mailid="p@gmail.com")
details(40,"chinnu","c@gmail.com")
details("bannu","b@gmail.com",30)
details(mailid="jun@gmail.com",id=50,name="junu")
# here we  are giving positional parameters so internally it searches in the callie function and matches them there
'''
#------------------------------------------------
#default arguments
'''
def grocery(item,price):
    print("item is %s " %item)
    print("price is %.2f " %price)
grocery("sugar",100)

def grocery(item="rice",price=1500):
    print("item is %s " %item)
    print("price is %.2f " %price)
grocery("sugar",100)

def grocery(item="rice",price=15000):
    print("item is %s " %item)
    print("price is %.2f " %price)
grocery()

def grocery(item,price=200):
    print("item is %s " %item)
    print("price is %.2f " %price)
grocery("dal")

def grocery(item="rice",price):
    print("item is %s " %item)
    print("price is %.2f " %price)
grocery(100)# error default args should be defied last and non defauld args should be in front of default

def grocery(price,item="rice"):
    print("item is %s " %item)
    print("price is %.2f " %price)
grocery(100)
'''
#task
#cake price qty
'''
def cakefun(cake,price=150.75,qty=1):
    print("cake is %s cake and its quantity is %d with price of %.2f" %(cake,qty,price))
cakefun("blueberry",200,2)
cakefun("blue berry")
cakefun("cheese",500,3)
cakefun("chocolate",qty=3)

def cakefun(cake="black",price=150.75,qty):
    print("cake is %s cake and its quantity is %d with price of %.2f" %(cake,qty,price))
cakefun(200,2)#gives error
'''

#star argument
#*argument --> * is used to unpack the elements
'''
a=[2,3,4,5,6,7]
print(a)
print(*a)
print(type(a))

a=(2,3,4,5,6,7)
print(a)
print(*a)
print(type(a))

a={2,3,4,5,6,7}
print(a)
print(*a)
print(type(a))

a={"name":"lokesh","year":2026,"month":"mar"}
print(a)
print(*a)# provides key in a dictionary
print(type(a))

a,b,c=1,2,3
print(a)
print(b)
print(c)

a,b,c=1,2,3,4,5,6,7,8
print(a)
print(b)
print(c)#error because we cannot unpack 8 values into 3--> variables(a,b,c), so we can use * argument here

a,b,*c=1,2,3,4,5,6,7,8
print(a)
print(b)
print(*c)

*a,b,c=1,2,3,4,5,6,7,8
print(*a)
print(b)
print(c)

a,b,c="codegnan"# cannot unpack 8 letters into 3 variables
print(a,b,c)

a,*b,c="codegnan"
print(a)
print(*b)
print(c)
'''
#task
#presentees and absentees
"""
no of students-4
ask each students present or not 
1-p
2-a
3-a
4-p
5-a
print report of present and absent

n=int(input("entre no od students"))
p=a=0
for i in range(n):
    print("student no :",i+1)
    k=input("entre if present or not")
    if k=='p':
        p+=1
    else:
        a+=1
print("report")
print("present:",p)
print("absent:",a)
print("total students",n)
"""
