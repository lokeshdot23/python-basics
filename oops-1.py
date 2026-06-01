#oops
'''
class classname():
    name="xpxpxpx"
    age=float('inf')
    city='universe'
    def fname(self):
        print(self.name,self.age,self.city)
a=classname()
a.fname()
'''
'''
#class declaration
class Details():
    name='loki'
    age=25
    place='vja'
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()
'''
#object instantiation
class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.data('lokesh',24,'vja')
print(dir(a))
a.display()
b=Details()
b.data('loki',30,'hyd')
b.display()
c=Details()
c.data("pannu",25,'vja')
c.display()
