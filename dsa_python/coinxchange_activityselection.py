#activity selection
'''
n=int(input("Enter the number of activities: "))
activities=[]
for i in range(n):
    start,end=map(int,input("Enter the start and end time: ").split())
    activities.append((start,end))
activities.sort(key=lambda x:x[1])
last=-1
for activity in activities:
    if activity[0]>last:
        print("selected acitivity:",activity)
        print("start time:",activity[0],end=" ")
        last=activity[1]

Output:
Enter the number of activities: 6
Enter the start and end time: 1 2
Enter the start and end time: 3 4
Enter the start and end time: 0 6
Enter the start and end time: 5 7
Enter the start and end time: 8 9
Enter the start and end time: 9 0
selected acitivity: (9, 0)
start time: 9 selected acitivity: (1, 2)
start time: 1 selected acitivity: (3, 4)
start time: 3 selected acitivity: (5, 7)
start time: 5 selected acitivity: (8, 9)
start time: 8
'''

#coin exchange of denominations by greedy approach

coins=[20,10,5,2,1]
amount=int(input('enter amount'))
count=0
for coin in coins:
    while amount>=coin:
        print(coin)
        amount-=coin
        count+=1
print(count)

