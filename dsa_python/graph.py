#graph
'''
#tanking input for an unweighted graph
graph={}
n=int(input("enter number of vertices"))
for i in range(n):
    vertex = input("enter vertiex: ")
    adj_vertex = input("enter adjcent vertices: ").split()
    graph[vertex]=adj_vertex
for vertex in graph:
    print(vertex,'->',graph[vertex])
'''
#taking input for a weighted graph
'''
graph = {}
n= int(input("enter number of vertices: "))
for i in range(n):
    vertex = input("Enter vertex: ")
    adj_vertex = int(input("enter adjcent vertices : "))
    graph[vertex]=[]
    for j in range(adj_vertex):
        neighbor = input("enter adjcent vertex: ")
        weight = int(input("enter weight: "))
        graph[vertex].append((neighbor,weight))
for vertex in graph:
    print(vertex,'->',graph[vertex])
'''
'''
#BFS - Breadth first search - Queue


graph = {}
n = int(input("Enter no. of vertices: "))
for i in range(n):
    vertex = input("Enter vertex: ")
    adj_vertex = input("Enter adjacent vertices: ").split()
    graph[vertex] = adj_vertex
start = input("Enter starting vertex: ")
queue = []
visited = []
queue.append(start)
visited.append(start)
while queue:
    current = queue.pop(0)
    print(current,end='->')
    for adj_vertex in graph[current]:
        if adj_vertex not in visited:
            visited.append(adj_vertex)
            queue.append(adj_vertex)
'''
#dfs
'''
graph={}
n=int(input("Enter the number:"))
for i in range(n):
    vertex=input("Enter vertex:")
    adj_vertex=input("Enter adjcent vertices:").split()
    graph[vertex]=adj_vertex
start=input("Enter starting vertex:")

visited=[]

def dfs(vertex):
    visited.append(vertex)
    print(vertex,end=' ')
    for adj_vertex in graph[vertex]:
        if adj_vertex not in visited:
            dfs(adj_vertex)
    print("backtracking from",vertex)
dfs(start)
'''
