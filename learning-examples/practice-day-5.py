'''class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def printpoint(self):
        print(self.a,self.b)
pp=Point(1,2)
pp.printpoint()
'''
'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __gt__(self,other):
        return self.x>other.x and self.y>other.y
p1=Point(2,2)
p2=Point(1,1)
print(p1 > p2)
'''
'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
p1=Point(1,2)
p2=Point(1,2)
print(p1 !=  p2)
'''
