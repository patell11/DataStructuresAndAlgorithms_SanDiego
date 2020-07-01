#Uses python3

import sys
import queue


def shortet_paths(adj, cost, source_vertex):
    #write your code here
    distance = [10**19] * len(adj)
    parents = [None] * len(adj)
    negative_cycle_vertices = []

    reachable = [0] * len(adj)
    shortest = [1] * len(adj)

    distance[source_vertex] = 0
    for i in range(len(adj)):                    # outer loop that runs V times
        for vertex in range(len(adj)):             # inner loop to run for all the vertex in graph
            cost_index = 0                  # variable to access the cost for each neighbour of the current vertex
            #print("---->", i, vertex, distance)
            for neighbour in adj[vertex]:   # check for all the edges of current vertex
                neighbour_cost = cost[vertex][cost_index]
                # Relax the edges i.e update the cost if its less than the previous stored cost
                # the condition to check for the vertex with max size is to ensure that the source vertex is connected
                # with the current vertex
                if distance[vertex] != 10**19 and distance[neighbour] > distance[vertex] + neighbour_cost:
                    distance[neighbour] = distance[vertex] + neighbour_cost
                    parents[neighbour] = vertex
                    reachable[neighbour] = 1
                    if i == len(adj)-1:            # last iteration i.e Vth iteration
                        # add all the vertices which decreases in the last iteration to the negative cycle queue
                        negative_cycle_vertices.append(neighbour)
                        shortest[neighbour] = 0
                cost_index += 1


    # updates the reachable array - it covers the case for the self vertex
    for i in range(len(adj)):
        if distance[i] < 10**19:
            reachable[i] = 1

    """
    use the queue negative_cycle and do BFS to find all the vertices which can be part of the negative cycle 
    (infinite arbitrage). The reason we need to do the BFS is because there can be multiple negative cycles in 
    the graph
    """
    visited = [False] * len(adj)
    while negative_cycle_vertices:
        current_vertex = negative_cycle_vertices.pop(0)
        visited[current_vertex] = True
        shortest[current_vertex] = 0
        for neighbour in adj[current_vertex]:
            if visited[neighbour] is False:
                negative_cycle_vertices.append(neighbour)
                shortest[neighbour] = 0



    return distance, shortest, reachable



if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    source_vertex = int(input())
    # print("adj ", adj)
    # print("cost ", cost)
    distance, shortest, reachable = shortet_paths(adj, cost, source_vertex-1)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])




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
    # s = data[0]
    # s -= 1
    # distance = [10**19] * n
    # reachable = [0] * n
    # shortest = [1] * n
    # shortet_paths(adj, cost, s, distance, reachable, shortest)
    # for x in range(n):
    #     if reachable[x] == 0:
    #         print('*')
    #     elif shortest[x] == 0:
    #         print('-')
    #     else:
    #         print(distance[x])
    #
