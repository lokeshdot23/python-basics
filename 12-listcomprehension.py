#list comprehension
'''
a=["python","code","codegnan"]

b=str(a)
c=b.upper()
print(c)
'''
#syntax
#[expression for var in range/iterable]
'''
a=[i.upper() for i in a]
print(a)

#task 1
a=['vja','hyd','vza']
print([i.capitalize() for i in a])

#task2
a=[1,2,3,5,6,8,12,13]
print([i**2 for i in a])
#i*i or pow(i,2)

#task3
#if usage in list comprehension
#write a program that prints even nos till 20
print([i for i in range(21) if i%2==0])

#task4
#squares of even no in range
print([pow(i,2) for i in range(16) if i%2==0])

#task 5
a=['apple','banana','grapes','mango','kiwi','dragon','berry']
#print([i for i in a if 'a' in i])

#task 6
print([i for i in a if 'a' not in i])

# there is no elif usage in list component
# if else usage innlist component
# task 7
print([i**2 if i%2 ==0 else i*5 for i in range(31)])

a=[1,2,3,4,5]
b=[5,4,3,2,1]
print([a[i]+b[i] for i in range(5) ])
'''
