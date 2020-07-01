#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj, adj_reverse):
    result = []
    #write your code here
    visited = set()
    order = []
    # for each vertex in the graph explore their neighbour and add to the visited set and order stack
    for vertex in range(len(adj)):
        if vertex not in visited:
            dfsUtl(adj, visited, order, vertex)

    visited.clear()       # clear the visited set and use it for the reverse graph
    # use the order stack and explore all the vertex
    for i in range(len(order)-1, -1, -1):
        top = order[i]
        if top not in visited:
            result_subset = []    # create new list to store the vertices of the strongly connected components
            dfsUtlReverse(adj_reverse, visited, result_subset, top)
            result.append(result_subset)

    return result

def dfsUtl(adj, visited, order, vertex):
    current = vertex
    visited.add(current)
    # explore the neighbour of the current vertex
    for neighbour in adj[current]:
        if neighbour not in visited:
            dfsUtl(adj, visited, order, neighbour)
    # if all the neighbours are explored, add to the order stack
    order.append(current)

def dfsUtlReverse(adj_reverse, visited, result_subset, current_vertex):
    visited.add(current_vertex)
    result_subset.append(current_vertex+1)    # to store the actual value instead of the index value as stored in the adj list
    for neighbour in adj_reverse[current_vertex]:
        if neighbour not in visited:
            dfsUtlReverse(adj_reverse, visited, result_subset, neighbour)


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    adj_reverse = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj_reverse[b - 1].append(a - 1)
    result = number_of_strongly_connected_components(adj, adj_reverse)
    print(len(result))


    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # adj_reverse = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #     adj_reverse[b-1].append(a-1)
    # print(number_of_strongly_connected_components(adj, adj_reverse))
