#operator overriding
'''
class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other_obj):
        return self.a*other_obj.b
class B:
    def __init__(self,b):
        self.b=b
a_obj=A(5)
other_obj=B(4)
print(a_obj+other_obj)
'''
#method overloading
'''
class New:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is ",a+b+c)
        elif a!=None and b!=None:
            print("the prod is ",a*b)
        else:
            print("terminator...")
s=New()
s.sum()
s.sum(1,2,3)
s.sum(3,4)
'''
'''
class New:
    def sum(self,a=2,b=3,c=4):
        if a!=2 and b!=3 and c!=4:
            print("the sum is ",a+b+c)
        elif a!=2 and c==4:
            print("product is ",a*b)
        else:
            print("terminator...")
s=New()
s.sum()
s.sum(1,2,3)
s.sum(3,4)
'''
#method overriding
'''
class Animal:
    def speak(self):
        print("animal sounds")
class Dog:
    def speak(self):
        print("dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()
'''

class Vehicle:
    def ride(self):
        print("horn ,high speeds etc....")
class Bus:
    def ride(self):
        print("bus stops, passingers etc.....")
class Car:
    def ride(self):
        print("personal car good to have")
arr=[Vehicle(),Bus(),Car()]
for i in arr:
    i.ride()
