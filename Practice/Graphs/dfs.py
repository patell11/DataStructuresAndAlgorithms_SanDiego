
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def getVertices(self):
        for i in self.graph:
            print(i, self.graph[i])

    def dfsUtl(self, v, visited):

        visited[v] = True
        print(v, end = " ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfsUtl(i, visited)


    def dfs(self, v):
        visited = [False] * (max(self.graph)+1)

        self.dfsUtl(v, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.getVertices()

