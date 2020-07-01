#Uses python3

import sys

def dfs(adj, visited, order, current):
    #write your code here
    visited.add(current)
    for neighbour in adj[current]:
        if neighbour not in visited:
            dfs(adj, visited, order, neighbour)

    order.append(current)


def toposort(adj):
    visited = set()
    order = []
    #write your code here
    for current in range(len(adj)):
        if current not in visited:
            dfs(adj, visited, order, current)

    return order

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    #print(order)
    for i in range(len(order)):
        x = order.pop()
        print(x + 1, end=' ')

