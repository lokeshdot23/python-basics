#Loops
#for,while,range,break,continue,pass
#for loop
'''
a=[10,20,30,40,50]
for in a:
    print(i)
print(type(a))
print(type(i))
a=[10,20,30,40,50]
for in a:
    print(i, end=" ")
a=(3,4,5,6,7)
for i in a:
    print(i)
    print(type(a))
    print(type(i))
a={1,2,3,4,5,6}
for i in a:
    print(i)
    print(type(a))
    print(type(i))
d={"year":2026,"month":"mar","date":7}
for i in d:
    print(i) # prints keys
for i in d.keys():
    print(i)#prints keys
    print(type(d))
    print(type(i))
for i in d.values():
    print(i)#prints values
    print(type(d))
    print(type(i))
for i in d.items():
    print(i)
    print(type(d))
    print(type(i))

a='codegnan'
for i in a :
    print(i,end="")
print(type(a))
print(type(i))

d={"year":2026,"month":"mar","date":7}
for i,j in d.items():
    print(i,j)

a=['apple','banana','mango']
for i in a:
    print(i)
    print(type(a))
    print(type(i))
a=[3,4.5,"loki",4+6j,True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))
'''
#----------------------
'''
a=['codegnan','python','course']

b=[]
for i in a:
    b.append(i.upper())
print(b)

#-----------------------------
a=['codegnan','python','course']
print('[',end="")
for i in a:
    print('"',end="")
    print(i.upper(),end='",')
print(']')

#-----------------------------
a=['codegnan','python','course']
b=str(a)
c=b.upper()
print(c)
'''
