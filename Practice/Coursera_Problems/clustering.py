
import math

class Item:
    def __init__(self, x, y, parent, rank):
        self.x = x
        self.y = y
        self.parent = parent
        self.rank = rank

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class DisjointSet:
    def __init__(self):
        self.vertex = []
        self.edges = []

    def makeSet(self, item):
        self.vertex.append(item)

    def addEdge(self, edge):
        self.edges.append(edge)

    def sortEdges(self):
        return sorted(self.edges)

    def find(self, point_index):
        if self.vertex[point_index].parent != point_index:
            self.vertex[point_index].parent = self.find(self.vertex[point_index].parent)
        return self.vertex[point_index].parent

    def union(self, index_1, index_2):
        rep_index_1 = self.find(index_1)
        rep_index_2 = self.find(index_2)

        rank_rep_1 = self.vertex[rep_index_1].rank
        rank_rep_2 = self.vertex[rep_index_2].rank

        if rep_index_1 == rep_index_2:
            return

        if rank_rep_1 > rank_rep_2:
            self.vertex[rep_index_2].parent = rep_index_1
        else:
            self.vertex[rep_index_1].parent = rep_index_2
            if rank_rep_2 == rank_rep_1:
                self.vertex[rep_index_2].rank += 1


def clustering(points, n_clusters):

    disjoint_set = DisjointSet()
    for i in range(len(points)):
        disjoint_set.makeSet(Item(points[i][0], points[i][1], i, 0))

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            disjoint_set.addEdge(Edge(i, j, getDistance(points[i], points[j])))

    sorted_edges = disjoint_set.sortEdges()

    result = 0
    for edge in sorted_edges:
        rep_start = disjoint_set.find(edge.start)
        rep_end = disjoint_set.find(edge.end)
        if rep_start != rep_end:
            disjoint_set.union(edge.start, edge.end)
            result += 1
        if result > len(points) - n_clusters:
            return edge.weight

    for edge in sorted_edges:
        print(edge.weight)
    print("result = ", result)
    return -1


def getDistance(point_1, point_2):
    return math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)


if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x,y = map(int, input(). split())
        points.append((x,y))                # tuple of points
    clusters = int(input())
    print("{0:.9f}".format(clustering(points, clusters)))