#Uses python3
import sys
import math
import heapq

def minimum_distance(points):

    costs = [float('inf')] * len(points)            # store the costs for each points
    min_heap = []                                   # use min heap to get the minimum distance
    for i in range(len(points)):                    # stores tuple of (distance, index)
        min_heap.append((float('inf'),i))

    min_heap[0] = (0, 0)
    costs[0] = 0

    while min_heap:
        current_point = heapq.heappop(min_heap)     # get the index with min distance
        #print("cufrrent point " , current_point)
        for i in range(len(min_heap)):              # check for all the other indices in the min heap
            neighbour_point = min_heap[i]
            distance = get_distance(points[current_point[1]], points[neighbour_point[1]])
            #print("   neighbour_point and distance ", neighbour_point, distance)

            # if the calculated distance is less than the current distance, update the distance in the min heap and in
            # the costs list. And then heapify to push the min distance up in the min heap list

            if neighbour_point[0] > distance:
                min_heap[i] = (distance, neighbour_point[1])
                costs[neighbour_point[1]] = distance
                #print("     costs ", costs)
                heapq.heapify(min_heap)
                #print("     min heap ", min_heap)
    return sum(costs)


def get_distance(point_1, point_2):
    return math.sqrt(((point_1[0] - point_2[0])**2) + ((point_1[1] - point_2[1])**2))


if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x,y = map(int, input(). split())
        points.append((x,y))                # tuple of points
    print("{0:.9f}".format(minimum_distance(points)))
    #print(minimum_distance(points))

