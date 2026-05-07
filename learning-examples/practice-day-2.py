# lists
'''
matrix = [[0, 1], [2, 3]]
zeros = [0]*10
print(zeros)
print(matrix)
a=[1,2,3,4]
c=a+zeros
#----------------------------------
a=[1,2,3,4,5]
b=['a','b','c','d']
print(a[:3])
print(a[0:3])
print(a[::-1])
print(a[-1])
c=a+b
print(c)
print(c[::2])
nums=list(range(0,31))
print(nums[::3])
print(nums[::-1])
'''
#how to unpack a list
'''
nums=[1,2,3,4,5,6,4,7,8,8,10]
first,second,*others,last=nums
print(first,second,last)
print(others)

#enumerate
nums=[1,2,3]
for num in nums:
    print(num)
#in i want index of each item i will use enumerate which in each iteration gives me a tuple of index and value

for num in enumerate(nums):
    print(num[0],num[1])
for i,num in enumerate(nums):
    print(i,num)
'''
#add to list
'''
letters=['a','b','c']
letters.append('d')
letters.append('d')
letters.insert(0,'A')
#remove
letters.pop()
letters.pop(0)
letters.remove('a')
del letters[0:2]
letters.clear()
print(letters)
'''
