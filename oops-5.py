#abstraction
'''
class parent():
    def data(self):
        pass
obj1=parent()
obj1.data()

class parent():
    def data(self):
        print("python class")
obj1=parent()
obj1.data()
'''
'''
from abc import ABC ,abstractmethod
class parent(ABC):
    @abstractmethod
    def method1(self):
        print("codegnan")
obj1=parent()
obj1.method1()#error because abstract class dosent have normal method so when object created we do not have anymethods to call
'''
from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class child(parent):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=child()
obj1.method1()
obj1.method2()
obj1.method3()
