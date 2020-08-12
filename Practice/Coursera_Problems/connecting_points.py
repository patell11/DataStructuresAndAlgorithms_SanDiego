import heapq
import math

def minimum_distance(points):
    min_heap = []
    for i in range(len(points)):
        min_heap.append((float('inf'), i))

    costs = [float('inf')] * len(points)

    min_heap[0] = (0,0)
    costs[0] = 0

    while min_heap:
        current_point = heapq.heappop(min_heap)
        for i in range(len(min_heap)):
            neighbour_point = min_heap[i]
            distance = getDistance(points[current_point[1]], points[neighbour_point[1]])

            if neighbour_point[0] > distance:
                costs[neighbour_point[1]] = distance
                min_heap[i] = (distance, neighbour_point[1])
        heapq.heapify(min_heap)

    return sum(costs)

def getDistance(point_1, point_2):
    return math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x,y = map(int, input(). split())
        points.append((x,y))                # tuple of points
    print("{0:.9f}".format(minimum_distance(points)))
    #print(minimum_distance(points))
