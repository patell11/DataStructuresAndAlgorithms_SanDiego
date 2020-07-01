#Uses python3

import sys
import queue
import heapq

"""
Use the min heap to maintain the priority queue. 
"""

# Defined a class Node to store the vertex and the weight
class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


def distance(adj, cost, start, end):
    #write your code here
    min_heap = []
    distance = [-1] * len(adj)  #store the distance

    heapq.heappush(min_heap, (0, start))  # Tuple of (weight, vertex), as the min heap prioritize based on the weights
    distance[start] = 0

    while min_heap:
        #print("distance ", distance)
        # Pop the vertex with min weight i.e the distance in this case
        current = heapq.heappop(min_heap)   # returns the tuple of vertex and weight
        cost_index = 0                      # this index is for accessing the cost from the cost list

        # returns the distance when encountered the end vertex
        if end == current[1]:
            return distance[current[1]]

        for neighbour in adj[current[1]]:                   # neighbours of the current vertex
            neighbour_cost = cost[current[1]][cost_index]   # cost from the current vertex to neighbour
            # if the distance of the neighbour is not updated or the existing distance is greater than the distance from
            # the current vertex to the current neighbour
            if (distance[neighbour] == -1 or distance[neighbour] > distance[current[1]] + neighbour_cost):
                distance[neighbour] = distance[current[1]] + neighbour_cost   # update the current neighbour's cost
                heapq.heappush(min_heap, (distance[neighbour], neighbour))    # add it the min heap

            # increase the counter for the cost_index to access the cost for the next neighbour of the current vertex
            cost_index += 1

    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = map(int, input().split())
    #print("adj ", adj)
    #print("cost ", cost)
    print(distance(adj, cost, s-1, t-1))


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
    # s, t = data[0] - 1, data[1] - 1
    # print(distance(adj, cost, s, t))
