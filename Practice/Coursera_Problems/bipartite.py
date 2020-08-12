
def bipartite(adj):
    queue = []
    visited = [0] * len(adj)

    visited[0] = 1
    queue.append(0)

    while queue:
        current = queue.pop(0)
        for neighbour in adj[current]:
            if visited[neighbour] == visited[current]:
                return 0
            if visited[neighbour] == 0:
                visited[neighbour] = - visited[current]
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