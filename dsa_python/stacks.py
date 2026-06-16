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
'''
'''
#rev a string using stacks
s=input("enter a string: ")
stack=[]
for ch in s :
    stack.append(ch)
rev=''
while stack:
    rev+=stack.pop()
print("reversed string:",rev)
'''
'''
#Balanced paranthesis
s=input('enter braces')
stack=[]
balanced=True
for ch in s:
    if ch=='(':
        stack.append(ch)
    elif ch==')':
        if not stack :
            balanced=False
            break
        stack.pop()
if stack:
    balanced=False
if balanced:
    print('balanced')
else:
    print('not')
'''
#balance the parenthesis if  not balanced by add9
'''
s=input("enter the braceses:")
stack=[]
balanced=0
for ch in s:
    if ch=='(':
        stack.append(ch)
    elif ch ==')':
        if stack:
            stack.pop()
        else:
            balanced+=1
balanced='('*balanced+s+')'*len(stack)
print(balanced)
'''
'''
#balance the parenthesis if  not balanced by sub
s=input("enter the braceses:")
stack=[]
remove=set()
for i in range(len(s)):
    if s[i]=='(':
        stack.append(i)
    elif s[i]==')':
        if stack:
            stack.pop()
        else:
            remove.add(i)
while stack:
    remove.add(stack.pop())
result=""
for i in range(len(s)):
    if i not in remove:
        result+=s[i]
print(result)
'''
'''
#find binary
n=int(input())
stack=[]
while n>0:
    stack.append(n%2)
    n//=2
print("Binary",end="")
while stack:
    print(stack.pop(),end=' ')
'''
#n = int(input("Enter number of elements:"))
nums = list(map(int,input("Enter elements:" ).split()))
stack = []
for num in nums:
    while stack and stack[-1]>num:
        stack.pop()
    stack.append(num)
print(stack)
