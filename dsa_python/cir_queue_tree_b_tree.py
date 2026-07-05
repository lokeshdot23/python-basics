#Circular Queue operations
'''
size = int(input("Enter queue size: "))
queue = [None]*size
front = -1
rear = -1
while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    ch = int(input("Enter your choice: "))
    if ch==1:
        val = int(input("Enter value: "))
        if (rear+1)%size==front:
            print("Queue is full")
        elif front==-1:
            front=rear=0
            queue[rear]=val
        else:
            rear = (rear+1)%size
            queue[rear] = val
    elif ch==2:
        if front==-1:
            print("Queue is empty")
        elif front==rear:
            print("Deleted:",queue[front])
            front = (front+1)%size
    elif ch==3:
        if front==-1:
            print("Queue is empty")
        else:
            i = front
            while True:
                print(queue[i],end=' ')
                if i==rear:
                    break
                i = (i+1)%size
            print()
    elif ch==4:
        break
'''
#Tree - node,edge
# Binary Tree, Proper tree,Skewed tree(right,left), Red-black tree, AVL trees, N-arr tree
'''class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = node(10)
root.left = node(20)
root.right = node(30)
print("Root:",root.data)
print("Left:",root.left.data)
print("Right:",root.right.data)'''
'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
arr = list(map(int,input("Enter values: ").split()))
nodes = []
for num in arr:
    nodes.append(node(num))
for i in range(len(arr)):
    left = 2*i+1
    right = 2*i+2
    if left<len(arr):
        nodes[i].left = nodes[left]
    if right<len(arr):
        nodes[i].right = nodes[right]
root = nodes[0]
print("Root:",root.data)
print("Left:",root.left.data)
print("Right:",root.right.data)
print("Right of right:",root.right.right.data)
'''
