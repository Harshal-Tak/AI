no_of_nodes = int(input("Enter number of nodes: "))

graph = {}

for i in range(no_of_nodes):
    node = input("Enter node name: ")
    graph[node] = []
    no_of_neighb = int(input("Enter number of neighbours: "))
    lst = []
    for j in range(no_of_neighb):
        neighbour = input("Enter neighbour: ")
        lst.append(neighbour)
    graph[node] = lst
    
print(graph)

visited = set()

def bfs(graph,vertex,visited):
    visited.add(vertex)
    queue = []
    queue.append(vertex)
    
    while queue:
        v = queue.pop(0)
        print(v)
        
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

v = input("Enter vertex name: ")

if v in graph:
    bfs(graph,v,visited)
