from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, vertex):
        visited = [False] * len(self.graph)

        queue = []

        visited[vertex] = True
        queue.append(vertex)
        while queue:
            current = queue.pop(0)
            print(current, end = " ")
            for neighbour in self.graph[current]:
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    queue.append(neighbour)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.bfs(2)