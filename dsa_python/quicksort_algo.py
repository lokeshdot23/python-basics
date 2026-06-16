#quick sort
'''
def qsort(arr):
    if len(arr)<=1:
        return arr
    p=arr[len(arr)//2]
    left=[x for x in arr if x<p]
    right=[x for x in arr if x>p]
    middle =[x for x in arr if x==p]
    return qsort(left)+middle+qsort(right)
arr=list(map(int,input("enter elements:").split()))
print(qsort(arr))
'''
'''
#flip pancake sort
def flip(arr,k):
    arr[:k] = arr[:k][::-1]
def pancakesort(arr):
    n = len(arr)
    for size in range(n,1,-1):
        maxindex = arr.index(max(arr[:size]))
        if maxindex!=size-1:
            flip(arr,maxindex+1)
            flip(arr,size)
    return arr
arr = list(map(int,input("Enter elements: ").split()))
print(*pancakesort(arr))
'''
