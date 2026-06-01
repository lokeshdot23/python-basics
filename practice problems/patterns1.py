'''
*
**
***
****
2
****
***
**
*
3
*****
*****
*****
*****
4
   *
  * *
 * * *
'''
'''
for i in range(int(input("enter for rangle triangle"))):
               print('*'*(i+1))

for i in range(int(input("enter for rev r angle triangle")),-1,-1):
    print('*'*i)

sq=int(input("enter for a square"))
for i in range(sq):
    for j in range(sq):
        print('*',end="")
    print()
'''
n=int(input("enter for pyramid"))
for i in range(n):
    print(' '*(n-i-1),end='')
    print('* '*(i+1))
'''
n=int(input('rev'))
for i in range(n):
    print('*'*(n-i))
'''
