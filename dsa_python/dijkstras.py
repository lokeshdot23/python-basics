#dijkstras
'''
graph={
    'A':{'B':2,'C':4},
    'B':{'D':1},
    'C':{'D':3},
    'D':{}
    }
distance={
    'A':0,
    'B':-1,
    'C':-1,
    'D':-1
    }
visited=[]
while len(visited)<len(graph):
    current=None
    for vertex in graph:
        if vertex not in visited and distance[vertex]!=1:
            if current is None or distance[vertex]<distance[current]:
                current= vertex
    if current is None:
        break
    visited.append(current)
    for adj in graph[current]:
        newdist=distance[adj]+graph[current][adj]
        if distance[adj]==-1 or newdist<distance[adj]:
            distance[adj]=newdist
for vertex in distance:
    print(vertex,'=',distance[vertex])
'''
