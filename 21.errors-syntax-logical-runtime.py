#syntax error
'''
for i in range(20)
print(i)
'''
#run_time error
'''
a=int(input("a value"))
b=int(input("b value"))
print(a+b)# 10/0 or 10/string gives error -->zerodivision error value error
'''
#logical error
'''
a=4
b=10
if a>b:
    print("greater")
'''
#exception handeling
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("optional")
    finally:
        print("program ends")
