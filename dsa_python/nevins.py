#Nevins number or harshads number
while True:
    n=int(input('entre a number'))
    c,s=n,0
    while c!=0:
        s+=c%10
        c//=10
    if n%s==0:
        print('Nevis')
    else:
        print("not nevins")
