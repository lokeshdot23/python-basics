'''
class Details:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
detail=Details('lokesh',24,'vja')
print(dir(detail))
detail.display()
'''
'''
#run-time imputs
class Details:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
detail=Details(input("enter your name"),int(input("enter your age")),input("enter your place"))
print(dir(detail))
detail.display()
'''
#diff between public var: _ and private var: __
'''
class Employee:
    def __init__(self):
        self.name='loki'
        self.__salary=10000
        self._mail='loki@gmail.com'
a=Employee()
print(dir(a))
print(a.name)
#print(a.__salary)#gets error for private variable
print(a._mail)
print(a._Employee__salary)
'''
'''
class Employee:
    def __init__(self,name,mail,salary):
        self.name=name
        self._mail=mail
        self.__salary=salary
    def display(self):
        print(self.name,self._mail,self.__salary)
e1=Employee('lokesh','lokesh@codegnan.in',29000)
e2=Employee('loki','loki@gmail.com',30000)
e1.display()
e2.display()
'''
'''
class Employee1:
    def __init__(self,name,mail,salary):
        self.name=name
        self._mail=mail
        self.__salary=salary
    def display(self):
        print(self.name,self._mail,self.__salary)
e1=Employee1('lokesh','lokesh@gmail.com',30000)
class Employee2:
    def __init__(self,name,mail,salary):
        self.name=name
        self._mail=mail
        self.__salary=salary
    def display(self):
        print(self.name,self._mail,self.__salary)
e2=Employee2('loki','loki@gmail.com',31000)
e1.display()
print(dir(e1))
e2.display()
print(dir(e2))
'''

#polymorphism
#operator overloading
a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(10))
print(a.__sub__(1))
print(a.__mul__(6))
#print(a.__div__(2))#gives error there is no __div__ magic method we have divmod and floordiv
print(a.__pow__(2))
print(a.__ge__(10))
print(a.__le__(20))
a=[1,2,3,4,5] ; b=[5,6,7,8,9,10,11]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a='python';b='course'
print(a.__add__(b))
a='code';b='gnan'
print(a.__add__(b))
print('pooja'.__add__(' mam'))
a='lokesh';b='m'
print(a.__add__(' '+b))
