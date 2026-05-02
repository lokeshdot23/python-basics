Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={2,3.4,"python",7+9j,True,False}
a
{False, True, 2, 3.4, (7+9j), 'python'}
type(a)
<class 'set'>
#add()
a={1,2,3,4,5)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a={1,2,3,4,5}
a.add{1}
SyntaxError: invalid syntax
a.add(1)
a
{1, 2, 3, 4, 5}
a.add(6)
a
{1, 2, 3, 4, 5, 6}
a.add(8)
a
{1, 2, 3, 4, 5, 6, 8}
a.add(7)
a
{1, 2, 3, 4, 5, 6, 7, 8}
#issubset and issuperset
a={1,2,3,4,5,6,7,8,9,0}
a
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
b={6,7,8,9,0}
b
{0, 6, 7, 8, 9}
b.issubset(a)
True
a.issubset(b)
False
b.issuperser(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b.issuperser(a)
AttributeError: 'set' object has no attribute 'issuperser'. Did you mean: 'issuperset'?
b.issuperset(a)
False
a.issuperset(b)
True
#union
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
a
{1, 2, 3, 4, 5, 6, 7}
b
{5, 6, 7, 8, 9, 10, 11}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
#intersection
a.intersection(b)
{5, 6, 7}
#prints the commpn values
#update()
a={1,2,3,4,5,6,7}
b=3,4,5,6,7,8,9,10,11,}
SyntaxError: unmatched '}'
b={3,4,5,6,7,8,9,10,11,}
type(b)
<class 'set'>
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
#difference
a={1,2,3,4,5,6}
b={3,4,5,6,7,8,9,10,11}
a.difference(b)
{1, 2}
a
{1, 2, 3, 4, 5, 6}
b.difference(a)#prints values that are not there in a
{7, 8, 9, 10, 11}
a={2,3,4,5,6,7}
b={1,5,6,7,8,9,10}
a.symmetric_difference(b)
{1, 2, 3, 4, 8, 9, 10}
#symmetric difference
a
{2, 3, 4, 5, 6, 7}
b
{1, 5, 6, 7, 8, 9, 10}
a.intersection_update(b)
a
{5, 6, 7}
#here we have updated a with intersection of a and b
#intersection_update
b.intersection_update(a)
b
{5, 6, 7}
#difference_update
a={4,5,6,7,8,9,10}
b={7,8,9,10,11,12,13}
a.difference_update(b)
a
{4, 5, 6}
b.difference_update(a)
b
{7, 8, 9, 10, 11, 12, 13}
a={3,4,5,6,7,8}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8}
#symmetric_difference_update removes common elements and updates
a={3,4,5,6,7,8,9,10,}
b={9,10,11,12,13,14}
c=a.copy()
c
{3, 4, 5, 6, 7, 8, 9, 10}
c.clear()
c
set()
a.add(10,20,33) # error one arg only typeerror
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.add(10,20,33) # error one arg only typeerror
TypeError: set.add() takes exactly one argument (3 given)
b.add(20)
b
{20, 9, 10, 11, 12, 13, 14}
b
{20, 9, 10, 11, 12, 13, 14}
c=list(b)
c
[20, 9, 10, 11, 12, 13, 14]
d=b+c
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    d=b+c
TypeError: unsupported operand type(s) for +: 'set' and 'list'
a={10,20,30,40,50}
a.pop()#randomly deletes a value
50
a.pop(10)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.pop(10)
TypeError: set.pop() takes no arguments (1 given)
a.pop(1)# Typeerror no args in pop
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a.pop(1)# Typeerror no args in pop
TypeError: set.pop() takes no arguments (1 given)
>>> #remove()
>>> #discard()
>>> a.remove(30)
>>> a
{20, 40, 10}
>>> a.discard(10)
>>> a
{20, 40}
>>> a.discard(10)
>>> a
{20, 40}
>>> a.remove(10)# error
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.remove(10)# error
KeyError: 10
>>> a=100,200,300,400}
SyntaxError: unmatched '}'
>>> a={100,200,300,400}
>>> b={300,400,500,600}
>>> a.isdisjoint(b)
False
>>> c
[20, 9, 10, 11, 12, 13, 14]
>>> d
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> a={1,2,3,}
>>> b={4,5,6,}
>>> a.isdisjoint(b)
True
>>> # isdisjoint gives if true if two sets are not subset of eachother that is if no value id matching
>>> len(a)
3
>>> a.count(2)# gives error because no method called count in sets as it dosent allow duplicated
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.count(2)# gives error because no method called count in sets as it dosent allow duplicated
AttributeError: 'set' object has no attribute 'count'
>>> a.index(2)# error no attribute such as index as it has no index and items are randomized in set
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a.index(2)# error no attribute such as index as it has no index and items are randomized in set
AttributeError: 'set' object has no attribute 'index'
