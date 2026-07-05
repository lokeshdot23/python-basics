#Tree Traversals
# In-order - Left->Root->Right  DBE|A|FCG
# Pre-order - Root->Left->Right ABDECFG
# Post order - Left->Right->Root DEBFGCA

#Pre-order traversal
'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def preorder(root):
    if(root):
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)
a = int(input("Enter root: "))
b = int(input("Enter left: "))
c = int(input("Enter right: "))
root = node(a)
root.left = node(b)
root.right = node(c)
preorder(root)
'''

#In-order traversal
'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
a = int(input("Enter root: "))
b = int(input("Enter left: "))
c = int(input("Enter right: "))
root = node(a)
root.left = node(b)
root.right = node(c)
inorder(root)
'''

#Post order traversal
'''
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def postorder(root):
    if(root):
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')
a = int(input("Enter root: "))
b = int(input("Enter left: "))
c = int(input("Enter right: "))
root = node(a)
root.left = node(b)
root.right = node(c)
postorder(root)
'''
'''
#Vertical Traversal
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def verticalTraversal(root):
    nodes = {}
    def traversal(node,row,col):
        if node is None:
            return
        if col not in nodes:
            nodes[col] = []
        nodes[col].append((row,node.data))
        traversal(node.left, row+1, col-1)
        traversal(node.right, row+1, col+1)
    traversal(root,0,0)
    for col in sorted(nodes.keys()):
        nodes[col].sort()
        print("Column",col,":",end=' ')
        for row,value in nodes[col]:
            print(value,end=' ')
        print()
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.right.left = Node("D")
verticalTraversal(root)
'''
#views of a tree
#left view ,right view ,top view ,bottom view
#left view
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def leftview(root,level):
    global max_level
    if root is None:
        return
    if level>max_level:
        print(root.data,end=' ')
        max_level=level
    leftview(root.left,level+1)
    leftview(root.right,level+1)
root=Node('a')
root.left=Node('b')
root.right=Node('c')
root.right.left=Node('d')
max_level=0
leftview(root,1)
'''

#left view
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def rightview(root,level):
    global max_level
    if root is None:
        return
    if level>max_level:
        print(root.data,end=' ')
        max_level=level
    rightview(root.right,level+1)
    rightview(root.left,level+1)
root=Node('a')
root.left=Node('b')
root.right=Node('c')
root.right.left=Node('d')
max_level=0
rightview(root,1)
'''
'''
#Top view of a tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def topview(root):
    q = [(root,0)]
    d = {}
    while q:
        node,hd = q.pop()
        if hd not in d:
            d[hd] = node.data
        if node.left:
            q.append((node.right,hd-1))
        if node.right:
            q.append((node.right,hd+1))
    for i in sorted(d):
        print(d[i],end=' ')
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.right.right = node(5)
topview(root)
'''
#Boundary traversal of a tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def leftboundary(root):
    if root:
        if root.left:
            print(root.data,end=' ')
            leftboundary(root.left)
        elif root.right:
            print(root.data,end=' ')
            leftboundary(root.right)
def leafnodes(root):
    if root:
        leafnodes(root.left)
        if root.left is None and root.right is None:
            print(root.data,end=' ')
        leafnodes(root.right)
def rightboundary(root):
    if root:
        if root.right:
            print(root.data,end=' ')
            rightboundary(root.right)
        elif root.left:
            print(root.data,end=' ')
            rightboundary(root.left)
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.right = node(6)
root.right.left = node(7)
print(root.data,end=' ')
leftboundary(root.left)
leafnodes(root.left)
leafnodes(root.right)
rightboundary(root.right)
