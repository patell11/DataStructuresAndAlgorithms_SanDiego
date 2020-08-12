
import sys

def negativeCycle(adj, cost):
    distance = [sys.maxsize] * len(adj)
    parents = [None] * len(adj)

    distance[0] = 0
    for i in range(len(adj)-1):
        for vertex in range(len(adj)):
            cost_index = 0
            for neighbour in adj[vertex]:
                neighbour_cost = cost[vertex][cost_index]
                if distance[neighbour] > distance[vertex] + neighbour_cost:
                    distance[neighbour] = distance[vertex] + neighbour_cost
                    parents[neighbour] = vertex
                cost_index += 1

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
    print(negativeCycle(adj, cost))