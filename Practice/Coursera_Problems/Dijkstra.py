
import heapq

def minimumCost(adj, weights, start, end):
    distance = [-1] * len(adj)
    distance[start] = 0

    minHeap = []
    heapq.heappush(minHeap, (0, start))

    while minHeap:
        current = heapq.heappop(minHeap)
        weight_index = 0

        if end == current[1]:
            return distance[current[1]]

        for neighbour in adj[current[1]]:
            neighbour_weight = weights[current[1]][weight_index]
            if distance[neighbour] == -1 or distance[neighbour] > distance[current[1]] + neighbour_weight:
                distance[neighbour] = distance[current[1]]+neighbour_weight
                heapq.heappush(minHeap, (distance[neighbour], neighbour))

            weight_index += 1

    return -2


if __name__ == '__main__':
    vertices, edges = map(int, input().split())
    adj = [[] for _ in range(vertices)]
    weights = [[] for _ in range(vertices)]
    for i in range(edges):
        u, v, w = map(int, input().split())
        adj[u-1].append(v-1)
        weights[u-1].append(w)
    start, end = map(int, input().split())
    print(minimumCost(adj, weights, start-1, end-1))