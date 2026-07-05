#reverse an array with two pointerr approach
'''
arr=list(map(int,input("enter elements : ").split()))
left =0
right =len(arr)-1
while left <right:
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
print(*arr)
'''
#palindrome function returns true or false
'''
def is_palindrome(text: str) -> bool:
    # Initialize two pointers
    left = 0
    right = len(text) - 1
    
    # Move pointers toward the middle
    while left < right:
        # If characters don't match, it is not a palindrome
        if text[left] != text[right]:
            return False
        
        # Move pointers closer
        left += 1
        right -= 1
        
    return True
print(is_palindrome("lol"))
'''
'''
#move 0's to one side
# 2 0 4 0 3 0 0 1 ==> 2 4 3 1 0 0 0 0
#2 pointer from start fast/slow 1- side
arr = list(map(int,input("enter numbers ").split()))
slow= 0
for fast in range(len(arr)):
    if arr[fast]!=0:
        arr[slow],arr[fast] =arr[fast],arr[slow]
        slow+=1
print(*arr)
'''
'''
#remove duplicates from a sorted arr
#1 1 2 3 4 4 ==> 1 2 3 4
arr = list(map(int,input("enter numbers: ").split()))
slow =0
for fast in range(1,len(arr)):
    if arr[fast]!=arr[slow]:
        slow+=1
        arr[slow]=arr[fast]
for i in range(slow+1):
    print(arr[i],end=' ')
'''
#sliding window
'''
arr = list(map(int,input('Enter values: ').split()))
slide =int(input("enter slide size: "))
windowsum=0
for i in range(slide):
    windowsum+=arr[i]
maxsum = windowsum
for i in range(slide,len(arr)):
    windowsum=windowsum-arr[i-silde]+arr[i]
    if windowsum >maxsum:
        maxsum=windowsum
print(maxsum)
'''
#sliding window anagram
'''
text = input("enter text :")
pattern = input("enter anagram pattern: ")
k= len(pattern)
count = 0
pattern_count = {}
for ch in pattern:
    if ch in pattern_count :
        pattern_count[ch]+=1
    else:
        pattern_count[ch]=1
windowcount = {}
for i in range(k):
    ch=text[i]
    if ch in windowcount:
        windowcount[ch]+=1
    else:
        windowcount[ch]=1
if windowcount == pattern_count:
    count+=1
for i in range(k,len(text)):
    leftchar = text[i-k]
    windowcount[leftchar]-=1
    if windowcount[leftchar]==0:
        del windowcount[leftchar]
    rightchar=text[i]
    if rightchar in windowcount:
        windowcount[rightchar]+=1
    else:
        windowcount[rightchar]=1
    if windowcount == pattern_count:
        count+=1
print(count)
'''
'''you have 2 baskets and each basket can hold only 1 type of fruit
find the max numbers of consective fruits you can collect while having at
most 2 fruits
apple orange apple orange banana orange orange apple
max=4
using silding window approach
'''
'''
arr=input().split()
left=0
fruit={}
maximum=0
for right in range(len(arr)):
    if arr[right] in fruit:
        fruit[arr[right]]+=1
    else:
        fruit[arr[right]]=1
    while len(fruit)>2:
        fruit[arr[left]]-=1
        if fruit[arr[left]]==0:
            del fruit[arr[left]]
        left+=1
    maximum=max(maximum,right-left+1)
print(maximum)
'''





















