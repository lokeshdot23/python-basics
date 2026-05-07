#fizzbuzz problem using python
def fizbuz(n):
    if n<=2:
        return 0
    fizz=0;buzz=0
    if(n%3==0):
        fizz=1
    if(n%5==0):
        buzz=1
    if(fizz==1 and buzz==1):
        return 3
    elif (fizz ==1):
        return 1
    elif (buzz==1):
        return 2
    else:
        return n

while True:
    n=int(input("entre a num"))
    msg=fizbuz(n)
    if msg==1:
        print("Fizz")
    elif msg==2:
        print("Buzz")
    elif msg==3:
        print("FizzBuzz")
    else:
        print(n)
