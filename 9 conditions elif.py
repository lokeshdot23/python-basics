#if elin else
'''
a=4;b=8
if a<b:
    print('less')
elif b>a:
    print('greater')
else:
    print('true')

a=4;b=8
if a==b:
    print('less')
elif b>a:
    print('greater')
else:
    print('true')

a=4;b=8
if a==b:
    print('less')
elif b<a:
    print('greater')
else:
    print('true')

a=8;b=8
if a<b:
    print('less')
elif b>a:
    print('greater')
elif a==b:
    print('equal')
else:
    print('true')

#logical

a=4;b=8
if a<b and b>a:
    print('less')
elif b>a and a<b:
    print('greater')
else:
    print('true')

a=4;b=8
if a<b and a>b:
    print('less')
elif b>a and a<b:
    print('greater')
else:
    print('true')

a=4;b=8
if a<b and b<a:
    print('less')
elif b>a and a>b:
    print('greater')
else:
    print('true')

a=4;b=8
if a<b or a<b:
    print('less')
elif b>a or a<b:
    print('greater')
else:
    print('true')

a=4;b=8
if a>b or b<a:
    print('less')
elif b>a or a>b:
    print('greater')
else:
    print('true')

a=4;b=8
if a>b or b<a:
    print('less')
elif b<a or a>b:
    print('greater')
else:
    print('true')
#identity

a=4;b=8
if type(a) is int:
    print('less')
elif type(a) is int:
    print('greater')
else:
    print('true')

a=4;b=8
if type(a) is not int:
    print('less')
elif type(a) is int:
    print('greater')
else:
    print('true')

a=4;b=8
if type(a) is not int:
    print('less')
elif type(a) is not int:
    print('greater')
else:
    print('true')

#membership

a='str'
if 's' in a:
    print("yes")
elif 't' in a:
    print('yes')
else:
    print('no')

a='str'
if 'k' in a:
    print("yes")
elif 't' in a:
    print('yes t present')
else:
    print('no')

a='str'
if 'k' in a:
    print("yes")
elif 'tl' in a:
    print('yes')
else:
    print('no')
'''
#multiple if
'''
a=8;b=10
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print('not equal')

a=8;b=10
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print('not equal')
'''
#logical
'''
a=8;b=10
if a<b and a>b:
    print("less")
if b>a or a<b:
    print("greater")
if a!=b:
    print('not equal')

#membership
a='str'
if 's' not in 'str':
    print("no s")
if 's' in 'str':
    print("s")
if 't' in 'str':
    print("t")

#identity
a=8;b=10
if type(a) is float:
    print("less")
if type(a) is not int:
    print("greater")
if type(a) is int:
    print('not equal')
'''
#nested if elif else
'''
a=5;b=10
if a<b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("true")

a=5;b=10
if a==b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("true")

a=5;b=10
if a<b:
    print("less")
    if b<a:
        print("greater")
    else:
        print("true")

a=5;b=10
if a<b:
    print("less")
    if b>a:
        print("greater")
    if a!=b:
        print("true")

a=5;b=10
if a<b:
    print("less")
    if b<a:
        print("greater")
    if a!=b:
        print("true")

a=5;b=10
if a>b:
    print("less")
    if b>a:
        print("greater")
    if a!=b:
        print("true")

a=5;b=10
if a>b:
    print("less")
    if b>a:
        print("greater")
    if a!=b:
        print("true")
    else:
        print("etrur")
else:
    print("outer else")

a=5;b=10
if a<b:
    print("less")
    if b==a:
        print("greater")
    elif a!=b:
        print("true")
'''
'''
#---------------------------------------------------
#problems

#voting
while True:
    age = int(input("entre age for eligibility check"))
    if age >= 18:
        print("eligible for vote")
    else:
        print("not eligible")

# even odd
    num = int(input("give an integer to check if its even or odd"))
    if num%2 == 0:
        print('even number')
    else:
        print("not even")

# leap year
    year = int(input("entre year"))
    if year%4 == 0:
        print("leap year")
    else:
        print("not a leap year")
'''
'''
#Vowels and consonent
str = input("entre a letter").lower()
if str in 'aeiou':
    print('it is a vowel')
else:
    print('it is a consonant')
# guest code
name =input("entre your name")
if name == 'loki':
    print (f'welcome {name}')
else:
    print('welcome guest')

#guest code for multiple guests
name = input("entre your name").lower()
names_of_family = ['loki','siddi','chinnu','junnu','bunnu','raju']
if name in names_of_family:
    print(f'welcome {name}')
else:
    print('welcome guest')
'''
'''
#social media login -username -password

if username and password matched "login successful"
if not matched "invalid credentials"

user='loki'
password='P1234'
verify_user=input('entre username ')
verify_pass=input('entre password ')
if(user == verify_user):
    if(password == verify_pass):
        print('login successful')
    else:
        print('invalid password')
else:
    print('invalid username')
'''
