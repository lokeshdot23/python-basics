#Expressions using stack
#Infix to prefix expression
'''
def precedence(op):
    if op in ('+','-'):
        return 1
    if op in ('*','/'):
        return 2
    if op in ('^'):
        return 3
    return 0
def infixtoprefix(expr):
    expr = expr[::-1]
    temp=''
    for ch in expr:
        if ch=='(':
            temp+=')'
        elif ch==')':
            temp+='('
        else:
            temp+=ch
    stack = []
    postfix = ''
    for ch in temp:
        if ch.isalnum():
            postfix+=ch
        elif ch=='(':
            stack.append(ch)
        elif ch==')':
            while stack and stack[-1]!='(':
                postfix+=stack.pop()
            stack.pop()
        else:
            while (stack and precedence(stack[-1])>=precedence(ch)):
                postfix+=stack.pop()
            stack.append(ch)
    while stack:
        postfix+=stack.pop()
    prefix = postfix[::-1]
    return prefix
expr = input("Enter an infix expression: ")
print("Prefix expression:",infixtoprefix(expr))
'''
'''
#Evaluation of prefix expression *+234->20

stack = []
expr = input("Enter expression: ")
for i in reversed(expr):
    if i.isdigit():
        stack.append(int(i))
    else:
        one = stack.pop()
        two = stack.pop()
        if i=='+':
            stack.append(one+two)
        elif i=='-':
            stack.append(one-two)
        elif i=='*':
            stack.append(one*two)
        elif i=='/':
            stack.append(one//two)
print(stack.pop())
'''
#Conversion of infix to postfix

def precedence(op):
    if op in '+-':
        return 1
    if op in '*/':
        return 2
    return 0
infix = input("Enter expression: ")
stack = []
postfix=''
for ch in infix:
    if ch.isalnum():
        postfix+=ch
    else:
        while stack and precedence(stack[-1])>=precedence(ch):
            postfix+=stack.pop()
        stack.append(ch)
while stack:
    postfix+=stack.pop()
print(postfix)
