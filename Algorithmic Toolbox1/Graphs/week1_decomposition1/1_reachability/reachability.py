#Uses python3

import sys
import fileinput


"""
Recursively call the reachUtl function to check for the to_ present in the adj[from_]. The visited index is marked
True in the visited list
"""

def reachUtl(adj, from_, to_, visited):
    #print(from_ ,to_, adj[from_])
    if from_ == to_:
        return 1

    for item in adj[from_]:
        if not visited[item]:
            visited[item] = True
            result = reachUtl(adj, item, to_, visited)
            if result == 1:
                return 1

    return 0

def reach(adj, x, y):
    #write your code here
    from_ = x
    to_ = y
    visited = [False] * len(adj)
    visited[from_] = True
    return reachUtl(adj, from_, to_, visited)


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    x, y = map(int, input().split())
    #print(adj)
    print(reach(adj, x-1, y-1))


    # input = fileinput.input()
    # data = list(map(int, input.split()))
    # print(data)
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # x, y = data[2 * m:]
    # adj = [[] for _ in range(n)]
    # x, y = x - 1, y - 1
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #     adj[b - 1].append(a - 1)
    # print(reach(adj, x, y))
