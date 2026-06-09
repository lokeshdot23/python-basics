while True:
    def even(n):
        print(n, 'in even')
        if n==0:
            print("Even")
        else:
            odd(n-1)
    def odd(n):
        print(n,'in odd')
        if n==0:
            print("Odd")
        else:
            even(n-1)
    n = int(input("Value: "))
    even(n)
