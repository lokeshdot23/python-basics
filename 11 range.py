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
'''
#student marks
'''
while True:
    marks = int(input("entre student marks:"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(50,71):
        print("Grade-D")
    else:
        print("Fail, you need more practice....,:)")
'''
