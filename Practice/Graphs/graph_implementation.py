

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def addNeighbour(self, nbr, weight = 0):
        self.connected_to[nbr] = weight

    def getConnections(self):
        return self.connected_to.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connected_to[nbr]

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def addVertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def getVertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def addEdge(self,from_, to_, weight=0):
        if from_ not in self.vert_list:
            nv = self.addVertex(from_)
        if to_ not in self.vert_list:
            nv = self.addVertex(to_)
        self.vert_list[from_].addNeighbour(self.vert_list[to_], weight)

    def getVertices(self):
        return self.vert_list.keys()

g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vert_list)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g.vert_list:
    for e in g.getVertex(v).getConnections():
    #print(g.getVertex(v).getConnections())
    #for e in v.getConnections():
        print("(%s, %s)" % (v, e.getId()))
