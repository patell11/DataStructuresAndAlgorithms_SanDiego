

def stronglyConnectedComponent(adj, adj_reversed, vertices):
    visited = [False] * vertices
    stack = []

    for i in range(vertices):
        current = i
        if not visited[current]:
            dfs(current, adj, visited, stack)

    visited = [False] * vertices
    result = []
    for element in stack:
        if not visited[element]:
            result_subset = []
            dfs_reversed(element, adj_reversed, visited, result_subset)
            result.append(result_subset)
    return result


def dfs_reversed(element, adj_reversed, visited,result_subset):
    visited[element] = True
    result_subset.append(element)
    for neighbour in adj_reversed[element]:
        if not visited[neighbour]:
            dfs_reversed(neighbour, adj_reversed, visited, result_subset)


def dfs(current, adj, visited, stack):
    visited[current] = True
    for neighbour in adj[current]:
        if not visited[neighbour]:
            dfs(neighbour, adj, visited, stack)
    stack.insert(0, current)


if __name__ == '__main__':
    vertices, edges = map(int, input().split())
    adj = [[] for _ in range(edges)]
    adj_reversed = [[] for _ in range(edges)]
    for i in range(edges):
        u,v = map(int, input().split())
        adj[u-1].append(v-1)
        adj_reversed[v-1].append(u-1)
    print(stronglyConnectedComponent(adj, adj_reversed, vertices))
