Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #List[]
>>> a=[4,6.5,"str",5+9j,True,False]
>>> print(a)
[4, 6.5, 'str', (5+9j), True, False]
>>> type(a)
<class 'list'>
>>> c=[8.9]
>>> type(c)
<class 'list'>
>>> a.append("html")
>>> a
[4, 6.5, 'str', (5+9j), True, False, 'html']
>>> a.append("java","guvi")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.append("java","guvi")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["css","js"])
>>> a
[4, 6.5, 'str', (5+9j), True, False, 'html', ['css', 'js']]
>>> a.extend(["loki","gupta","siddi","aasi"])
>>> a
[4, 6.5, 'str', (5+9j), True, False, 'html', ['css', 'js'], 'loki', 'gupta', 'siddi', 'aasi']
>>> a.insert(0,"1st pos changed")
>>> a
['1st pos changed', 4, 6.5, 'str', (5+9j), True, False, 'html', ['css', 'js'], 'loki', 'gupta', 'siddi', 'aasi']
>>> a=["apple","banana"]
>>> a.insert(0,"mango")
>>> a
['mango', 'apple', 'banana']
>>> # extend and insert in the above lines
>>> #index()
>>> a=(["a","b","c","d")]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> a=(["a","b","c","d"])
>>> a
['a', 'b', 'c', 'd']
>>> a.index('b')
1
>>> #copy()
>>> b=a.copy()
>>> b
['a', 'b', 'c', 'd']
>>> #clear
>>> a.clear()
a
[]
a.extend(b)
a
['a', 'b', 'c', 'd']
#sort
a=["white","black","pink","gold","orange"]
a.sort()
a
['black', 'gold', 'orange', 'pink', 'white']
b=[1,5,66,3,,44,1,2,1,4,90,2234,45,1,6,7,343,1.1]
SyntaxError: invalid syntax
b=[1,5,66,3,2.3,44,1,2,1,4,90,2234,45,1,6,7,343,1.1]
b.sort()
b
[1, 1, 1, 1, 1.1, 2, 2.3, 3, 4, 5, 6, 7, 44, 45, 66, 90, 343, 2234]
#reverse()
a=["white","grey","pink","black"]
a.reverse()
a
['black', 'pink', 'grey', 'white']
a.reverse()
a
['white', 'grey', 'pink', 'black']
a.sort()
a
['black', 'grey', 'pink', 'white']
a.reverse()
a
['white', 'pink', 'grey', 'black']
b=[1,3,2,4,5,3,6,6,67,76,67,76,88,44,90,1]
b
[1, 3, 2, 4, 5, 3, 6, 6, 67, 76, 67, 76, 88, 44, 90, 1]
b.reverse()
b
[1, 90, 44, 88, 76, 67, 76, 67, 6, 6, 3, 5, 4, 2, 3, 1]
b.sort()
b
[1, 1, 2, 3, 3, 4, 5, 6, 6, 44, 67, 67, 76, 76, 88, 90]
b.reverse()
b
[90, 88, 76, 76, 67, 67, 44, 6, 6, 5, 4, 3, 3, 2, 1, 1]
b.sort().reverse()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    b.sort().reverse()
AttributeError: 'NoneType' object has no attribute 'reverse'
a.sort(reverse=True)
a
['white', 'pink', 'grey', 'black']
b
[1, 1, 2, 3, 3, 4, 5, 6, 6, 44, 67, 67, 76, 76, 88, 90]
b.sort(reverse=True)
b
[90, 88, 76, 76, 67, 67, 44, 6, 6, 5, 4, 3, 3, 2, 1, 1]
a=[6,2,3,1,5,6,2,22,5,7,8,22,33,22,55,33,78,9,98]
(a.sort).reverse()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    (a.sort).reverse()
AttributeError: 'builtin_function_or_method' object has no attribute 'reverse'
a
[6, 2, 3, 1, 5, 6, 2, 22, 5, 7, 8, 22, 33, 22, 55, 33, 78, 9, 98]
a.pop()
98
a
[6, 2, 3, 1, 5, 6, 2, 22, 5, 7, 8, 22, 33, 22, 55, 33, 78, 9]
a.pop(6)
2
a.remove(22)
a
[6, 2, 3, 1, 5, 6, 5, 7, 8, 22, 33, 22, 55, 33, 78, 9]
a.count()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
a.count("22")
0
len(a)
16
b="hello"
len(b)
5
b.count('l')
2
b=b.append("java")
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    b=b.append("java")
AttributeError: 'str' object has no attribute 'append'
c=[]
c.append(b)
c
['hello']
c.append(b)
c.extend(c)
c
['hello', 'hello', 'hello', 'hello']
c.count()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    c.count()
TypeError: list.count() takes exactly one argument (0 given)
c.count("hello")
4
a.count(22)
2
#tuple
a=(1,4,2,3,4,5,5,7.8,2,5)
a
(1, 4, 2, 3, 4, 5, 5, 7.8, 2, 5)
type(a)
<class 'tuple'>
b=3,7.8,"python",4+9j,True,False)
SyntaxError: unmatched ')'
b=(3,7.8,"python",4+9j,True,False)
b
(3, 7.8, 'python', (4+9j), True, False)
type(b)
<class 'tuple'>
len(b)
6
b.count('python')
1
a.count(5)
3
a=[9,1,5,2,8,4,6,3,7,0]
#7,6,4,3,0,9,8,5,2,1
len(a)
10
b=a[:5]
b
[9, 1, 5, 2, 8]
c=a[5:0]
c
[]
c=a[5:]
c
[4, 6, 3, 7, 0]
b.sort(reverse=True)
c.sort(reverse=True)
a
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
b
[9, 8, 5, 2, 1]
c
[7, 6, 4, 3, 0]
d=c.extend(b)
d
c.extend(b)
c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1, 9, 8, 5, 2, 1]
d=c[:10]
d
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
d=c+b
e=c+b
e
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1, 9, 8, 5, 2, 1, 9, 8, 5, 2, 1]
c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1, 9, 8, 5, 2, 1]
b
[9, 8, 5, 2, 1]
c=c[:5]
c
[7, 6, 4, 3, 0]
c+b
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
