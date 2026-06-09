import time
class Contact:
    def __init__(self,name,mobile,mail):
        self.name=name
        self.mobile=mobile
        self.mail=mail
lst=[]
def display():
    print("*" * 48)
    for i in lst:
        print(f"* {i.name:<15} {i.mobile:<12} {i.mail:<15} *")
    print("*" * 48)
while True:
    print('Menu'.center(30,'*'))
    print("1.Add contact\n2.Update contact\n3.Display list of contacts\n4.Remove contact\n5.Exit\n")
    n=input("enter your choice here: ")
    if n=='1':
        print('Adding contact module started')
        print('loading contact...')
        time.sleep(2)
        a,b,c=input("Enter name mobile number and email: ").split()
        lst.append(Contact(a,b,c))
        print("Contact added Successfully :)")
    elif n == '2':
        print("enter old contact number to search: ")
        number=input()
        for i in lst:
            if i.mobile==number:
                print("enter your new number: ")
                new_number=input()
                i.mobile=new_number
                display()
                print("new number updated to: ",new_number)
                print("new updated contact: "+"\nName: "+i.name+"\nMobile: "+i.mobile+"\nMail: "+i.mail)
            else:
                print("no such number exists")
    elif n=='3':
        display()
    elif n=='4':
        print("enter name to remove: ")
        nam=input()
        print("searching for",nam+'...')
        time.sleep(1)
        for i in lst:
            if i.name==nam:
                print("Found the user")
                print("Removed: ",i.name,'from the data')
                lst.remove(i)
                display()
                break
        else:
            print("User not found")
    elif n=='5':
        print("loading to exit...")
        time.sleep(2)
        print("Visit us again")
        break
