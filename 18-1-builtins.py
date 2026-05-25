#build in functions
#print, input, len, typr, range, min, max, sum
#fromkeys is a built in function only used for dictionary
#fromkeys convert single string into dictionary formate
a="codegnan"
'''print(a)
print(list(a))
print(tuple(a))
print(set(a))
print(dic(a))#error'''


'''b = dict.fromkeys(a)
print(b)
b= dict.fromkeys(a, "veerendra")
print(b)
b['c']= "python"
print(b)'''

#eval() eval is a builtin datatype
'''while True:
    a= int(input("a value"))
    b = int(input(" b value"))
    print(a+b)'''


'''while True:
    a= float(input("a value"))
    b = float(input(" b value"))
    print(a+b)'''
    
'''while True:
    a = eval(input("data1"))
    b = eval(input("data2"))
    print(a+b)'''
#zip()->we can combine multiple collections into one collection
#zip is a builtin function
#we have to use a datatype when using a bultin function
'''a= [10,20,30, 40,50]
names= ["apple","bannana","Mango"]
print(a+names)

b = list(zip(a,names))
print(b)

b= tuple(zip(a,names))
print(b)

b= set(zip(a, names))
print(b)

b= dict(zip(a, names))
print(b)'''

#enumerate ()->we can give conter to the collection
#it is a bultin function
'''names =["geethe","latha", "kalyan","Nani"]
for i in range(len(names)):
    print(i,names[i])
b= list(enumerate(names))
print(b)

b = list(enumerate(names,100))
print(b)

b = dict(enumerate(names))
print(b)

b = list(enumerate(names))
print(b)'''

#ASCII
#chr(),ord()

'''chr(56)
'8'
chr(90)
'Z'
chr(65)
'A'
ord("a")
97
'''
'''for i in range( ord("a"),ord("z")):
    print(i)

for i in range( ord("A"),ord("Z")):
    print(i)'''
#task 1
'''for i in range((input())):
    print(ord(i),end =" ")'''
#task 2
'''a = input()
for i in a:
    print(i ,"=",ord(i),end=" ")'''
