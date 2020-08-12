

def topologicalSort(adj):
    visited = [False] * len(adj)
    stack = []

    for i in range(len(adj)):
        current = i
        if not visited[current]:
            dfs(current, adj, visited, stack)
    return stack

def dfs(current, adj, visited, stack):
    visited[current] = True
    for neighbour in adj[current]:
        if not visited[neighbour]:
            dfs(neighbour, adj, visited, stack)
    stack.insert(0, current)



if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    result = topologicalSort(adj)
    for i in result:
        print(i+1)
