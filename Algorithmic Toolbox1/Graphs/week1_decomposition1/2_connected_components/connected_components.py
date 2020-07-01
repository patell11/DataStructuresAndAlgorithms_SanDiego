#Uses python3

import sys


def number_of_components(adj):
    result = 0
    #write your code here
    vertices = len(adj)
    visited = [False] * len(adj)
    for i in range(vertices):
        if visited[i] == False:
            result += 1
            dfs(adj,i, visited)

    return result

def dfs(adj, v, visited):
    for item in adj[v]:
        if not visited[item]:
            visited[item] = True
            dfs(adj, item, visited)

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #print(adj)
    print(number_of_components(adj))


    #
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #     adj[b - 1].append(a - 1)
    # print(number_of_components(adj))
