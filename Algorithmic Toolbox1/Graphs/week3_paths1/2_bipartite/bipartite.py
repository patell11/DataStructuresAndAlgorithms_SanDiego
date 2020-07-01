#Uses python3

import sys
#import queue

def bipartite(adj):
    #write your code here
    visited = [0] * len(adj)
    queue = []

    visited[0] = 1
    queue.append(0)

    while queue:
        current = queue.pop(0)
        for neighbour in adj[current]:
            if visited[neighbour] == visited[current]:  # If the neighbour value is same as the current value it should return as no bipartite
                return 0
            # if the neighbour is not visisted update the value to the opposite of the current value
            if visited[neighbour] == 0:
                visited[neighbour] = -visited[current]
                queue.append(neighbour)

    return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))


    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #     adj[b - 1].append(a - 1)
    # print(bipartite(adj))
