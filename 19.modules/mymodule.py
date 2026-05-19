#def greetings(name):
#    print(f'welcome {name}')
#a=20
#b=30
#print("sum is",a+b)
#print("mymodule")
'''
a=int(input())
b=int(input())
print("sum is" ,a+b)

details={
    "idno":[10,20,30],
    "names":['sita','gita','shila'],
    "marks":[60,70,80]}
'''
'''
if __name__=="__main__":
    a=[10,20,30,40]
    #a.append("code")
    a.extend("code")
    print(a)
'''
def checkscript():
    if __name__=='__main__':
        print("inside script")
    else:
        print("inside module")
        #this is printed when calling from different file as main
        #inside this dosent match the main inside this file
checkscript()
    
