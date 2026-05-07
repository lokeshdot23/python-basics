'''
a=[1,2,3,]
a.remove(4)#valueerror

a="(1,2,3,4)"
c=a.strip("()")
print(c)
#print(c.split(','))
b=list(map(int ,c.split(',')))
print(b)

a=10;b=20;c=30
a,b,c=20,30,10 #this is indirectly a tuple and we are unoaching it so this is how swapping works
print(a,b,c)

a=10;b=20;c=30
a,b,c=(20,30,10)
print(a,b,c)

a=10;b=20;c=30
a,b,c=20                #typeerror cannot unpack int obj
print(a,b,c)
'''
