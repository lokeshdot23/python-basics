#Heapq
'''import heapq
from collections
heappush()
heappop()
heappushpop()
heapreplace()
nlargest(2,arr)
nsmallest()
merge()
clear()
heapify()'''

'''import heapq
heap = []
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,30)
heapq.heappush(heap,40)
print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappushpop(heap,7))
print(heap)
print(heapq.heapreplace(heap,7))
print(heap)
print(heapq.nlargest(1,heap))
print(heapq.nsmallest(1,heap))
a = [1,2,3]
b = [4,5,6]
print(list(heapq.merge(a,b)))
heap.clear()
print(heap)
a = [1,2,3,4,5,6,7,22,89]
print(heapq.nlargest(3,a)[-1])
import heapq
arr = [5,2,8,1]
heapq.heapify(arr)
print(arr)'''
#minimum priority order
'''
import heapq
pq=[]
n=int(input("enter size"))
for i in range(n):
    val=int(input("enter values: "))
    heapq.heappush(pq,val)
print("\nmin priority queue")
print("\nelements removed in min priority order")
while pq:
    print(heapq.heappop(pq),end=" ")
'''
'''
import heapq
pq=[]
n=int(input("enter size"))
for i in range(n):
    val=int(input("enter values: "))
    heapq.heappush(pq,-val)
print("\nmax priority queue")
print("\nelements removed in max priority order")
while pq:
    print(-heapq.heappop(pq),end=" ")
'''
'''
#nlargest function in heapq without using it
import heapq
pq=[]
n=int(input("enter size"))
for i in range(n):
    val=int(input("enter values: "))
    heapq.heappush(pq,-val)
print("\nmax priority queue")
print("\nelements removed in max priority order")
nlargest=int(input("enter nlargest"))
for i in range(nlargest):
    print(-heapq.heappop(pq),end=" ")
'''
'''
#kth largest element
arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[i]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr[j-k])
'''
