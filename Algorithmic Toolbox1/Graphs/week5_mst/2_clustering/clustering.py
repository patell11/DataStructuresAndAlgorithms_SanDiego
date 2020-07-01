#Uses python3
import sys
import math

class Item:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index                  # can be treated as the parent of the set
        self.rank = 0

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    # this function helps in sorting the class instances in the list i.e list of edges below
    def __lt__(self, other):
        return self.weight < other.weight

def getDistance(point_1, point_2):
    return math.sqrt(((point_1[0] - point_2[0]) ** 2) + ((point_1[1] - point_2[1]) ** 2))

def makeSet(x, y, index, nodes):
    nodes.append(Item(x, y, index))

def find(start, nodes):
    if nodes[start].index != start:
        nodes[start].index = find(nodes[start].index, nodes)
    return nodes[start].index

def union(start, end, nodes):
    rep_start = find(start, nodes)
    rep_end = find(end, nodes)

    rank_start = nodes[rep_start].rank
    rank_end = nodes[rep_end].rank

    if rep_start == rep_end:
        return

    if rank_start > rank_end:
        nodes[rep_end].index = rep_start
    elif rank_end > rank_start:
        nodes[rep_start].index = rep_end
    else:
        nodes[rep_end].index = rep_start
        nodes[rep_start].rank += 1



def clustering(points, n_clusters):
    #write your code here
    nodes = []              # stores each point with its index and rank
    edges = []              # stores the edges with its start and end vertex

    # make individual set for each point from the points list
    for i in range(len(points)):
        makeSet(points[i][0], points[i][1], i, nodes)

    # create edge connecting all the points
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            edges.append(Edge(i, j, getDistance(points[i], points[j])))

    edges = sorted(edges)
    #print(edges[0].weight)

    result = 0
    """
        N-1 th edge connects 2 clusters i.e, last edge added in the algorithm.(N-2) 
        and (N-1) edge connects 3 clusters i.e, the last before edge.Ans so on.
    """

    # Iterate through the sorted edges and find the clusters by using find and union technique of the disjoint sets
    # We check for the parents of each edge and if different cluster them.
    for edge in edges:
        rep_start = find(edge.start, nodes)
        rep_end = find(edge.end, nodes)
        if rep_start != rep_end:
            result += 1
            union(edge.start, edge.end, nodes)
        if result > len(points) - n_clusters:
            return edge.weight

    return -1


if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x,y = map(int, input(). split())
        points.append((x,y))                # tuple of points
    clusters = int(input())
    print("{0:.9f}".format(clustering(points, clusters)))

    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # data = data[1:]
    # x = data[0:2 * n:2]
    # y = data[1:2 * n:2]
    # data = data[2 * n:]
    # k = data[0]
    # print("{0:.9f}".format(clustering(x, y, k)))
