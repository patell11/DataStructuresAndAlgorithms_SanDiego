
def acyclic(adj):
    gray = []
    black = []

    for i in range(len(adj)):
        current = i
        if dfs(current, gray, black, adj):
            return True
        return False

def dfs(current, gray, black, adj):
    gray.append(current)
    for neighbour in adj[current]:
        if neighbour in black:
            continue
        if neighbour in gray:
            return True
        if dfs(neighbour, gray, black, adj):
            return True

    black.append(current)
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