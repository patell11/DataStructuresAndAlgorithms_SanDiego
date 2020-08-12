
def shortestDistance(adj, start, end):
    queue = []
    queue.append(start)

    distane = [-1] * len(adj)
    distane[start] = 0

    while queue:
        current = queue.pop(0)
        for neighbour in adj[current]:
            if distane[neighbour] == -1:
                distane[neighbour] = distane[current] + 1
                if neighbour == end:
                    return distane[end]
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
    print(shortestDistance(adj, x - 1, y - 1))