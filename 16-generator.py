#generator
#a=[expr for var in collection/range]

a=[i for i in range(21)]
print(a)

a=(i for i in range(21))
print(*a)
print(type(a))

a=(i for i in range(21))
print(list(a))
print(type(a))

a=(i for i in range(21))
print(set(a))
print(type(a))

a=(i for i in range(21))
print(type(tuple(a)))
print(type(a))

a={i:i*i for i in range(21)}
print((a))
print(type(a))
'''
'''
#Yield
a,b=[int(x) for x in input("enter a and b vals").split()]
def check (a,b):
    while a<b:
        yield a
        a+=1
        yield a
print(*check(a,b))

a,b=[int(x) for x in input("entre the values").split()]
def check(a,b):
    while a<b:
        a=a+1
        return a
#print(*check(a,b))#gives error
print(check(a,b))

#Yield vs return
def mygen():
    #return "java"
    #return "python"
    #return "dsa"
    return "java","python","dsa"
print(*mygen())#unpacks the tuple into seperated spaced vals

def mygen():
    yield "java"
    yield "python"
    yield "dsa"
print(*mygen())# unpacks the generator object

#next() in yield
def mygen():
    yield "java"
    yield "python"
    yield "dsa"
d=mygen()
print(next(d))
print(next(d))
print(next(d))
