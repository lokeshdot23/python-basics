#use.sort()
#sorted(list)
#or
#Bubble Sort
'''
arr=list(map(int,input().split()))
n=len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)
'''
#selection sort
'''
arr=list(map(int,input().split()))
n=len(arr)
for i in range(n-1):
    mi=i
    for j in range(i+1,n):
        if arr[j]<arr[mi]:
            mi=j
    arr[i],arr[mi]=arr[mi],arr[i]
print(*arr)
'''
