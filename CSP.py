class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
 
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True
 
        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
 
    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == None:
            return False
 
        print("Solution exist and Following are the assigned colours:")
        for c in colour:
            print(c, end=' ')
        return True

    
v = int(input("Enter number of vertices: "))
g = Graph(v)
grap = []

for row in range(0,v):
    for col in range(0,v):
        grap[row][col] = 0
        ch = int(input(f"Does edge exist between {col}{row}(1/0)?: "))
        if(ch == 1):
            grap[row][col] = grap[col][row] = 1
        else:
            grap[row][col] = grap[col][row] = 0

g.graph = grap
m = 3
 
g.graphColouring(m)
