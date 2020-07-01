#Uses python3

import sys
#import queue

def shotestDistance(adj, start, end):
    #write your code here
    distance = [-1]* len(adj)
    queue = []

    queue.append(start)
    distance[start] = 0
    #visited[start] = True
    while queue:
        #print("distance -",distance )
        current = queue.pop(0)
        for neighbour in adj[current]:
            if distance[neighbour] == -1:
                distance[neighbour] = distance[current] + 1    # distance of the parent vertex + 1
                if neighbour == end:
                    return distance[neighbour]

                queue.append(neighbour)

    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    x, y = map(int, input().split())
    #print(adj)
    print(shotestDistance(adj, x - 1, y - 1))

    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #     adj[b - 1].append(a - 1)
    # s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    # print(distance(adj, s, t))
