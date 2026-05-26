#file handling
#write mode
'''
a=open('lokesh.txt','w')
a.write("codegnan it solutions")
a.close()
'''
'''
#new file created if i use again w mode to write on same name
a=open('lokesh.txt','w')
a.write("Python language")
a.close()
#append
a=open('lokesh.txt','a')
a.write("\ncodegnan it solutions")
a.close()
#task to get data from runtime
n=input('data')
a=open('lokesh.txt','a')
a.write(n)
a.close()

#another method
a=open('lokesh.txt','a')
a.write(input('enter data'))
#print(a.readlines())#error cannot read on write or append mode
a.close()
'''
'''
#read module
#a=open('lokesh.txt')
#c=a.read()
#print(c)
#print(a.read())#reads all the text file
#print(a.readline())#readonly first line
#print(a.readlines())#stores line by line in list
#print(a.read(9))#gets first 9 characters
'''
#writelines() it prints every object side by side
'''a=['loki','loki1','loki2','loki3']
b=open('loki.txt','w')
b.writelines(a)
b.close()'''
'''
a=['loki','loki1','loki2','loki3']
b=open('loki.txt','w')
b.writelines('\n'.join(a))#joins all elements in list with \n so we get on newlines in the file
b.close()
'''
'''
a=open('data.py')#prints all the data indide that file
print(a.read())

a=open("E:\\codegnan\\python-basics\\19.modules\\mathmodinpython.py")

print(a.read())
a.close()
'''
#task train ticket
while True:
    ticket_price=1000
    print("New Customer")
    #print("**************************************")
    print("enter your gender: (M/F)")
    gender=input().upper()
    print("enter our age: ")
    age=int(input())
    if gender=='M':
        if age>=60:
            print("amount: ",(ticket_price-ticket_price*(30/100)))
        else:
            print("amount: ",ticket_price)
    else:
        if age>=60:
            print("amount: ",ticket_price*(50/100))
        else:
            print("amount: ",(ticket_price-ticket_price*(30/100)))
    print("======================================")
