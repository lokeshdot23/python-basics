#inheritance
#single inheritance
'''
class RBI:
    cash=100000
    def available_cash(cls):
        print("available cash is ",cls.cash)
        print("available cash is ",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(cls):
        print("new cash is ",cls.cash+cls.cash)
        print("new cash is ",cls.cash+RBI.cash)
a=HDFC()
print(dir(a))
a.available_cash()
a.new_cash()
'''
#multiple inheritance
'''
class Father:
    def height(self):
        self.h=5.6
        return 'height:'+str(self.h)
class Mother:
    def weight(self):
        self.w=55
        return '\nweight:'+str(self.w)
class Kid(Father,Mother):
    def dob(self):
        self.d='11/8/2001'
        return '\ndate of birth:' + str(self.d)
a=Kid()
print(dir(a))
print(a.height(),a.weight(),a.dob())
'''
#multi level inheritance
'''
class GP:
    def land(self):
        print('land')
class P(GP):
    def house(self):
        print('house')
class C(P):
    def vehicle(self):
        print('vehicle')
a=C()
a.vehicle()
a.house()
a.land()
'''
#hierarchical inheritance
'''
class Employee:
    def cat(self):
        print("employees category")
class Trainer(Employee):
    def exp(self):
        print("Employee Trainer has experiance and knowledge")
class Developer(Employee):
    def skill(self):
        print("Employee developer has skills and experiance")
a=Trainer()
a.cat()
a.exp()
b=Developer()
b.cat()
b.skill()
'''
#hybrid
#ex:1
'''
class Employee:
    def cat(self):
        print("employees category")
class Trainer(Employee):
    def exp(self):
        print("Employee Trainer has experiance and knowledge")
class Developer(Employee):
    def skill(self):
        print("Employee developer has skills and experiance")
class Work(Trainer,Developer):
    def load(self):
        print("have work")


w=Work()
w.load()
w.exp()
w.skill()
w.cat()
'''
#ex:2
'''
class Person:
    def details(self):
        print("name is lokesh")
class Trainer(Person):
    def teach(self):
        print("python")
class Student(Person):
    def learning(self):
        print("learn the code")
class Management(Trainer,Student):
    def manage(self):
        print("codegnan")
a=Management()
a.details()
a.teach()
a.learning()
a.manage()
'''
#super()
'''
class parent:
    def __init__(self,name):
        self.name=name
        print(name,"in parent constructor")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print(age,"age in child class")
a=child("loki",23)

'''
#encapsulation
'''
#public data
class parent:
    pub_data=100
    def method1(self):
        print(self.pub_data)
class child(parent):
    def method2(self):
        print(self.pub_data)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1.pub_data)
'''
#protected data no use _ is treated as variable name
'''
class parent:
    _pro_data=100
    def method1(self):
        print(self._pro_data)
class child(parent):
    def method2(self):
        print(self._pro_data)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._pro_data)
'''
'''
#private data
class parent:
    __pri_data=100
    def method1(self):
        print(self.__pri_data)
class child(parent):
    def method2(self):
        #print(self.__pri_data)#error because var is private
        print(self._parent__pri_data)
a=child()
a.method1()
a.method2()
print(a._parent__pri_data)

'''
'''
class parent:
    def __init__(self,name):
        self.name=name
        print(name,"in parent constructor")

class child(parent):
    def __init__(self,name,age):
        # super().__init__(name)
        self.age=age
        #super().__init__(name)
        print(age,"age in child class")
        super().__init__(name)
a=child("loki",23)
'''
