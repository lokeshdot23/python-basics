#stack operationss
'''
stack=[]
items=int(input("Enter element to push"))
stack.append(item)
print(stack)

stack=[]
elements=list(map(int,input().split()))
for element in elements:
    stack.append(element)
print(stack)
'''
'''size
stack=[]
n=int(input("enter size"))
for i in range(n):
    v=int(input("enter values"))
    stack.append(v)
print(stack)

if len(stack)==0:
    print("emptystack")
else:
    print("popped element:",stack.pop())
print(stack)
print("peek element",stack[-1])
'''
'''
stack=[]
size=int(input("stack size:"))
for i in range(size+1):
    item=int(input("enter num:"))
    if len(stack)==size:
        print("stack overflow...")
        break
    else:
        stack.append(item)
print("stack",*stack)
'''
stack=[]
max_len=3
def push(item):
    if len(stack)==max_len:
        print("stack overflow")
    else:
        stack.append(item)
        print(item,"pushed")

for i in range(4):
    push(i)
