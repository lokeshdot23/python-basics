#function withou using lambda
'''
def cal(n):
    return (n*2)+5
print(cal(int(input())))
'''
#annonymous functions(nameless functions)
#syntax
#a=lambda arg:expr
'''
a=lambda x:2*x+5
print(a(5))

a=int(input("entre a value"))
b=lambda x:2*x+5
print(b(a))
'''
'''
#task
a="codegnan"
b=lambda x:x.upper()
print(b(a))
# runtime
a=input()
b=lambda x:x.upper()
print(b(a))
#task 2
a="python course"
b=lambda x:x.title()
print(b(a))
#runtime
a=input()
b=lambda x:x.title()
print(b(a))
'''
'''
a=input()
b=input()
c=lambda a,b:a+" "+b
print(c(a,b))
'''
'''
a,b=[i for i in input("enter nums").split()]
c=lambda a,b:a+' '+b
print(c(a,b))
'''
#filters
'''
a=[5,6,7,8,9,10,20,30,37,86,67,59]

for i in a:
    if i%2==0:
        print(i)

b=list(filter(lambda a:a%2==0,a))
print(b)
'''
#[],{},(),set()
'''
a=[]
print(type(a))
print(type({}))
print(type(()))
print(type(set()))
'''
#filter none values
'''
a=[[],{},(),set(),"",None,3,4.8,8+9j,True,"loki",False]
b=list(filter(None,a))
print(b)
'''
#print(eval(input()))
#map()
#map-->each object from collection and forma a new collection
'''
a=[3,4,5,6,8,9,10,11]
b=[1,2,4,7,9,10,11,12]
c=list(map(max,a,b))
d=list(map(min,a,b))
print(c,d)
'''
'''
a=input("data1")
b=input("data2")
print(a+b)
a,b=input("enter the values").split(",")
print(a+b)

a,b=[x for x in input("enter the names").split(",")]
print(a,b)
'''
#list integer input using map
'''
a=int(input())
b=int(input())
print(a+b)
'''
'''
a,b=int(input("enter the values").split())
print(a+b)#error int cannot be applied to both values
'''
#we can use list comprehension as well
#a,b=[int(x) for x in input().split()]
#print(a,b)
#so we use map here
'''
a,b=map(int,input().split())
print(a+b)
a=list(map(int,input().split()))
print(a)
a=set(map(int,input().split()))
print(a)
a=tuple(map(int,input().split()))
print(a)
'''
#a=dict(map (str:int,input().split(",")))#map is not needed for dict input
a=input()
b=dict(i.split(":") for i in a.split(","))
print(b)
