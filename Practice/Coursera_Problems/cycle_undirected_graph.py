
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.visited = set()

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def findCycle(self):
        for vertex in self.graph:
            if vertex not in self.visited:
                if self.findCycleUtl(vertex, -1):
                    return True
        return False

    def findCycleUtl(self, vertex, parent):
        print("vertex and parent = ", vertex, parent)
        self.visited.add(vertex)
        for neighbour in self.graph[vertex]:
            if neighbour not in self.visited:

                if self.findCycleUtl(neighbour, vertex):
                    return True
            elif parent != neighbour:
                print("Entering here for", vertex, parent, neighbour)
                return True
        print("False for ", vertex, parent)
        return False

g = Graph(6)
g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('B', 'C')
#g.addEdge('B', 'E')
g.addEdge('C', 'D')
g.addEdge('D', 'E')
print(g.graph)
print(g.findCycle())

