#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    distance = [sys.maxsize] * len(adj)   # assign max value to the list of length adj
    parents = [None] * len(adj)           # stores the parent of a vertex

    distance[0] = 0
    for i in range(len(adj)-1):                    # outer loop that runs V-1 times
        for vertex in range(len(adj)):             # inner loop to run for all the vertex in graph
            cost_index = 0                  # variable to access the cost for each neighbour of the current vertex
            for neighbour in adj[vertex]:   # check for all the edges of current vertex
                neighbour_cost = cost[vertex][cost_index]
                # Relax the edges i.e update the cost if its less than the previous stored cost
                if distance[neighbour] > distance[vertex] + neighbour_cost:
                    distance[neighbour] = distance[vertex] + neighbour_cost
                    parents[neighbour] = vertex
                cost_index += 1

    # Relax all edges again and if we get any edge decreasing it means there exists a negative cycle
    for vertex in range(len(adj)):
        cost_index = 0
        for neighbour in adj[vertex]:
            neighbour_cost = cost[vertex][cost_index]
            if distance[neighbour] > distance[vertex] + neighbour_cost:
                return 1
            cost_index += 1
    return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    # print("adj ", adj)
    # print("cost ", cost)
    print(negative_cycle(adj, cost))


    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    # data = data[3 * m:]
    # adj = [[] for _ in range(n)]
    # cost = [[] for _ in range(n)]
    # for ((a, b), w) in edges:
    #     adj[a - 1].append(b - 1)
    #     cost[a - 1].append(w)
    # print(negative_cycle(adj, cost))
