#Uses python3

import sys


def acyclic(adj):

    gray = set()
    black = set()

    for i in range(len(adj)):
        current = i
        if dfs(current, adj, gray, black) == True:
            return True

    return False

def dfs(current, adj, gray, black):
    gray.add(current)
    for neighbour in adj[current]:
        if neighbour in black:
            continue
        if neighbour in gray:
            return True
        if dfs(neighbour, adj, gray, black) == True:
            return True
    black.add(current)
    return False


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    #print(adj)
    if acyclic(adj):
        print(1)
    else:
        print(0)
