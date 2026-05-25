#regular expressions(regex)
'''
a="codegnan is in vijayawada"
print(a)
a="codegnan \nis \tin \nvijayawada"
print(a)
#rstring
a=r"codegnan is in vijayawada"
print(a)
'''
#compile(),search(),findall(),split(),sub()
#sequesce characters
'''
\w->it matches alphanumeric
\W->it matches non-alpha-numeric
\d->it matches any digit
\D-> it matches non digit
\s->it represents white spaces
\S-> it reprsents non-white spaces
'''
import re
a="map maths cat cash money cup cap mug codegnan"
'''
b=re.compile(r"m\w\w\w")
print(b)#prints re.compile('m\\w\\w\\w')

#search
c=b.search(a)
print(c)
'''
'''
c=re.search(r'm\w+',a)
print(c)
'''
'''
#findall()
b=re.findall(r'm\w+',a)
print(b)
'''
'''
#task
#search c
c=re.findall('c\w+',a)
print(c)
'''
#split()
'''
b=re.split(r'm',a)
print(b)
'''
'''
b=re.split(r'\s',a)
print(b)
'''
#sub
'''
a=re.sub(r"maths","science",a)
print(a)

a=re.sub("maths","science",a)
print(a)
'''
'''
a='11223344556677889900'
b=re.split('\d1',a)
print(b)
'''
a='11223344522566227788992200'
'''
b=re.findall('\d\d22',a)
print(b)#prints['1122', '4522', '6622', '9922']
'''
'''
b=re.findall('\d2',a)
print(b)#['12', '52', '62', '92']
'''
