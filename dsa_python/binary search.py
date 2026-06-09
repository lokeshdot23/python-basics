# Binary Search patterns:
'''
1. Binary Search - find mid value
2. Lower bound pattern
3. Upper bound pattern
4. First occurrence
5. Last occurrence
6. Peak element
7. Answer range

We can perform all these operations in sorted order only.
monotonic data -> increasing or decreasing order
bitonic ->  1 3 5 4 2 . Here 1->3 increasing and 4->2 decresing 5 is the peak element viceversa
'''
#1
'''
arr=list(map(int,input().split()))
target=int(input())
left=0
right=len(arr)-1
found=False
while left<=right:
    mid = (left+right)//2
    if arr[mid] == target:
        print("Element found at index",mid)
        found = True
        break
    elif arr[mid]<target:
        left = mid+1
    else:
        right = mid-1
if not found:
    print("Element not found...")
'''
#2
'''
arr = list(map(int,input("Enter values: ").split()))
target = int(input("Enter target: "))
left = 0
right = len(arr)-1
ans = len(arr)
while left<=right:
    mid = (left+right)//2
    if arr[mid] >= target:
        ans = mid
        right = mid-1
    else:
        left = mid+1
print("Lower bound",ans)
'''

#3
'''
arr = list(map(int,input("Enter values: ").split()))
target = int(input("Enter target: "))
left = 0
right = len(arr)-1
ans = len(arr)
while left<=right:
    mid = (left+right)//2
    if arr[mid] > target:
        ans = mid
        right = mid-1
    else:
        left = mid+1
print("Upper bound",ans)
'''
#4
'''
arr = list(map(int,input("Enter values: ").split()))
target = int(input("Enter target: "))
left = 0
right = len(arr)-1
first = -1
while left<=right:
    mid = (left+right)//2
    if arr[mid] == target:
        first = mid
        right = mid-1
    elif arr[mid]<target:
        left = mid+1
    else:
        right = mid-1
print("First occurrence",first)
'''

#5
'''
arr = list(map(int, input("Enter values: ").split()))
target = int(input("Enter target: "))
left = 0
right = len(arr) - 1
last = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        last = mid
        left = mid+1      
    elif arr[mid] < target:
        left = mid+1
    else:
        right = mid-1
print("Last occurrence:", last)
'''
#6
'''
target=int(input())
left=0
found=False
element=0
right=target//2
while left<=right:
    mid=(left+right)//2
    if mid*mid==target:
        print("element found")
        found=True
        element=mid
        break
    elif mid*mid<target:
        left=mid+1
    else:
        right=mid-1
if found:
    print("element is:",element)
else:
    print("Square root daniki raaduu raa pichiiii")
'''
#7
