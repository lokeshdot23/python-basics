#range
'''
start-stop-step
for i in range(10):
    print(i)
for i in range(1,16):
    print(i)
for i in range(5,26):
    print(i)

for i in range(2,10):
    print(i*2,end=" , ")
print()
for i in range(0,30,3):
    print(i,end=" , ")
print()
for i in range(5,50,5):
    print(i,end=" , ")

#student marks
while True:
    marks = int(input("entre student marks:"))
    if marks in range(91,102):
        print("Grade-A")
    elif marks in range(81,92):
        print("Grade-B")
    elif marks in range(71,82):
        print("Grade-C")
    elif marks in range(50,72):
        print("Grade-D")
    else:
        print("Fail")

'''
'''
#break
a=30
while a>5:
    print(a)
    a-=1
    if a==15:
        break
a=30
while a>5:
    a-=1
    if a==15:
        break
    print(a)
a=30
while a>5:
    a-=1
    if a==15:
        break
print(a)
for i in range(19):
    if i==10:
        break
    print(i)
a="python"
for i in a:
    if i=='o':
        break
    print (i)
'''
#continue
'''
a=30
while a>0:
    a-=1
    print(a)
    if a==15:
        continue
a=30
while a>0:
    a-=1
    if a==15:
        continue
    print(a)
for i in range(15):
    if i==12:
        continue
    print(i)

for i in "python":
    if i=='t':
        continue
    print(i)
'''
#pass
'''
a=30
while a>1:
    a-=1
    if a==15:
        pass
    print(a)

for i in range(5):
    if 1==2:
        pass
    print(i)
'''
