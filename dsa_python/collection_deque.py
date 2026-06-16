#deque
'''
#Deque - Double ended queue
Left Deletion
Right Insertion
Insertion and deletion can be performed on both sides

import deque -> collections
operations:
    append()  1 2 3 <- 4  1 2 3 4
    appendleft()  4-> 1 2 3   4 1 2 3
    pop()  1 2 3 4->4  1 2 3
    popleft()  1 2 3 4   2 3 4
'''
'''
from collections import deque

arr=[1,2,3,4,5]
d=deque(arr)
d.append(10)
d.append(20)
d.appendleft(30)
d.appendleft(60)
print("display")
for data in d:
    print(data,end=' ')
d.rotate(-2)
print("after rotating")
print()
for data in d:
    print(data,end=' ')
print()
print("popping element",d.pop())
print("popping element left",d.popleft())
print("after popping")
for data in d:
    print(data,end=' ')

#maxlength
print()
print("maxlen in a deque")
dque2=deque(maxlen=3)
dque2.append(2)
dque2.append(3)
dque2.append(4)
dque2.append(5)
#what we expect 2 3 4 5 but we get 3 4 5 as a result because it follows fifo whn we specify maxlen and drops the first element
for dd in dque2:
    print(dd,end=' ')
print("count of an element")
print(dque2.count(4))
print("reverse")
print(dque2.reverse())
print("extend")
dque2.extend([10,20,30])
print(dque2)
print("in extend left elements dose extend in the given order insted they go in reverse order")
dque2.extendleft([90,100,110])
print(dque2)
print("clear clears the data")
dque2.clear()
print(dque2)
'''
#write a program to check if a string arr is palindrome or not using deque
from collections import deque
'''
str1=input("enter to check if palindrome").split()
ln=len(str1)
str1=deque(str1)
#5          0 1 2 3 4
check=0
for i in range(ln//2):
    if str1.popleft()==str1.pop():
        continue
    else:
        check=1
        print("not a palindrome")
        break
if not check:
    print("palindrome")
'''
str2=input("enter to get reverse ").split()
rev=''
ln=len(str2)
for i in range(ln):
    rev+=str2.pop()
print(rev)
