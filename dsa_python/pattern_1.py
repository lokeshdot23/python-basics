#pattern
n=int(input("give a number"))

print('1st question')
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
print()
print('2nd question')
#middle empty only last lines and side lines
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print("3rd question")
print()
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or j+i==n-1 or i==j:
            print('*',end=" ")
        else:
            print(' ',end=' ')
    print()
