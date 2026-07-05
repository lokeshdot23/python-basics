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
'''
#n = int(input("Enter number of elements:"))
nums = list(map(int,input("Enter elements:" ).split()))
stack = []
for num in nums:
    while stack and stack[-1]>num:
        stack.pop()
    stack.append(num)
print(stack)
'''
#Stack condition whether it's empty or full
'''stack=[]
n=int(input('enter the size of the stack'))
for i in range(n):
    v=int(input('enter the value'))
    stack.append(v)
stack.append(11)
stack.append(22)
stack.append(33)
print(*stack)
print('removed',stack.pop())
print('peak',stack[-1])
print('size',len(stack))'''

'''Max= int(input("Enter stack size: "))
stack=[]
n= int(input("Enter number of elements: "))
for i in range(n):
    if len(stack)<Max:
        stack.append(int(input()))
    else:
        print("stack overflow")
        break
print("Stack:", stack)
if len(stack)==0:
    print("Stack is Empty ...")
else:
    print("Stack is not Empty.")

if len(stack)==Max:
    print("Stack is Full")
else:
    print("Stack is not full")'''
#Implementations of stack

'''
1. Monotonic stack
2. Increasing
3. Decreasing
4. Valid paranthesis
 i. Check balanced
 ii. Balance the unbalanced
 iii. Delete the balanced

Increasing monotonic stack

bottom -> 3 1 4 2 6 8 ->top
[]->push 3
[3]->push 1? is 3 smaller than 1 false -> pop()
[]
[1] -> push 1
[1]->push 4 > is 4 greater than 1 true ->push 4
[1,4] -> push 2? is 2 greater than 4 -> pop 4
[1] -> push 1
[1,2] -> 2 -> 6
[1,2,6] 6>2 T
[1,2,6,8] 8>6 T

i/p: 3 1 4 2 6 8
o/p: 1 2 6 8
'''

#Increasing monotonic stack
'''stack = []
nums = list(map(int,input("Enter values: ").split()))
for x in nums:
    while stack and stack[-1]>x:
        stack.pop()
    stack.append(x)
print(stack)'''

#Decreasing monotonic stack
'''stack = []
nums = list(map(int,input("Enter values: ").split()))
for x in nums:
    while stack and stack[-1]<x:
        stack.pop()
    stack.append(x)
print(stack)'''

#Bitonic stack
'''stack = []
nums = list(map(int,input("Enter values: ").split()))
for i in range(0,len(nums),2):
    print(nums[i],end=' ')
for i in range(1,len(nums),2):
    stack.append(nums[i])
while stack:
    print(stack.pop(),end=' ')

#Balanced paranthesis or not
s = input("Enter expression: ")
stack = []
pairs = {')':'(',']':'[','}':'{'}
balanced = True
for ch in s:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack or stack[-1]!=pairs[ch]:
            balanced = False
            break
        stack.pop()
if stack:
    balanced = False
if balanced:
    print(s,"is balanced")
else:
    print(s,"is not balanced")
'''
'''
s = input("Enter expression: ")
stack = []
pairs = {')': '(', ']': '[', '}': '{'}
rev_pairs = {'(': ')', '[': ']', '{': '}'}
result = []

for ch in s:
    if ch in '([{':
        stack.append(ch)
        result.append(ch)
    elif ch in ')]}':
        if stack and stack[-1] == pairs[ch]:
            stack.pop()
            result.append(ch)
        else:
            result.append(pairs[ch])
            result.append(ch)
    else:
        result.append(ch)
while stack:
    open_bracket = stack.pop()
    result.append(rev_pairs[open_bracket])

print("Balanced:", "".join(result))
'''
