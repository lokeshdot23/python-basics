import random
#sample and range
'''
a=random.sample(range(10,40),30)
print(a)
'''
#randint
'''
a=random.randint(30,40)
print(a)
'''
#choice
'''
a=[10,20,30,40,50,60,70,80,90]
b=random.choice(a)
print(b)
'''
#task
'''
s=True
while s:
    print("enter the roll of dies")
    n=int(input())
    print("options")
    print("1.yes \n2.no")
    m=input()
    if m == '1':
        print("dies shuffeled")
        print("generated value: ",random.randint(1,6))
        print("-----------------------------------")
    else:
        s=False
        print("-----------end of game-------------")
'''
