#creating a node
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(20)
n3=node(30)
n1.next=n2
n2.next=n3
head=n1
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
'''
#---------------------------------------------------------------------
#insert at end
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input("enter no of nodes"))
head=None
tail=None
for i in range(n):
    data=int(input("enter a value"))
    newnode=node(data)
    if head==None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
print("Single linked list")

temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
'''
#----------------------------------------------------------------------------
'''
#insert at begin
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input("enter no of nodes"))
head=None
tail=None
for i in range(n):
    data=int(input("enter a value"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("Single linked list")

temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
'''
#--------------------------------------------------------------------------------
# insert at begin and deleting at begin
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input("enter no of nodes"))
head=None
tail=None
for i in range(n):
    data=int(input("enter a value"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("Single linked list")

temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
#delete head
if head is None:
    print("empty ")
else:
    deleted=head.data
    head=head.next
    print("deleted element",deleted)
print("single ll after deleting at begin:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
'''
#-----------------------------------------------------------------------------------
'''
#insert at begin and delete at end
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input("enter no of nodes"))
head=None
tail=None
for i in range(n):
    data=int(input("enter a value"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("Single linked list")

temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
#delete end
if head is None:
    print("empty ")
elif head.next is None:
    deleted=head.data
    head=None
    print("deleted element",deleted)
else:
    temp=head
    while temp.next.next:
        temp=temp.next
    deleted=temp.next.data
    temp.next=None
    print("deleted element:",deleted)
print("single ll after deleting at end:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
'''
#todo task
'''
#insert at end and delete at end
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input("enter no of nodes"))
head=None
tail=None
for i in range(n):
    data=int(input("enter a value"))
    newnode=node(data)
    if head==None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
print("Single linked list")

temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
#deleting at end
if head is None:
    print("empty ")
elif head.next is None:
    deleted=head.data
    head=None
    print("deleted element",deleted)
else:
    temp=head
    while temp.next.next:
        temp=temp.next
    deleted=temp.next.data
    temp.next=None
    print("deleted element at end",deleted)
print("after deleting")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
'''
'''
#insert at end and delete at begin
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input("enter no of nodes"))
head=None
tail=None
for i in range(n):
    data=int(input("enter a value"))
    newnode=node(data)
    if head==None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
print("Single linked list")

temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
#code for delete at begin
if head is None:
    print("empty ")
else:
    deleted=head.data
    head=head.next
    print("deleted element",deleted)
print("single ll after deleting at begin:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
'''
''' positional insertion in sll'''
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input("enter no of nodes"))
head=None
tail=None
for i in range(n):
    data=int(input("enter a value"))
    newnode=node(data)
    if head==None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
print("Single linked list")

temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("None")
#code for insertion in the middle
data=int(input("enter value to be inserted"))
pos=int(input("enter at what position we need to insert"))
newnode=node(data)
if pos ==0:
    newnode.next=head
    head=newnode
else:
    current=head
    for _ in range(pos-1):
        current=current.next
    newnode.next=current.next
    current.next=newnode
current=head
while current:
    print(current.data,end='->')
    current=current.next
print("None")
'''
#delete at position
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input("enter no of nodes"))
head=None
tail=None
for i in range(n):
    data=int(input("enter a value"))
    newnode=node(data)
    if head==None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
print("Single linked list")
pos=int(input("enter a pos to delete at"))
if head is None:
    pass
elif pos==0:
    head=head.next
else:
    current=head
    for _ in range(pos-1):
        if current.next is None:
            break
        current=current.next
    if current.next:
        current.next=current.next.next
curr=head
while curr:
    print(curr.data,end='->')
    curr=curr.next
print('None')
