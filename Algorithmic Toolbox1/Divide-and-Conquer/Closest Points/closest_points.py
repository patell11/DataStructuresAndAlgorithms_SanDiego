# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


## function to calculate the minumum distances between the points
def bruteForce(points):
    d_min = distance_squared(points[0], points[1])
    length_points = len(points)
    if length_points == 2:
        return d_min

    for i in range(length_points-1):
        for j in range(i+1, length_points):
            if i !=0 and j != 1:
                d = distance_squared(points[i], points[j])
                d_min = min(d_min, d)
    return d_min

#print(mergeSort([Point(1,0), Point(3,5), Point(5,2), Point(6,4), Point(10,10)]))

## function to find the minimum distance for the points in the strip which are d i.e min_distances apart.
# def closestStripPair(points, min_distance):
#     mid = len(points) // 2
#     mid_x = points[mid].x               ## x co-ordinate of the mid point
#
#     # make a list of the points which are min_distances apart from the x co-ordinate of the mid point
#     strips = [point for point in points if mid_x - min_distance <= point.x <= mid_x + min_distance ]
#
#     # sort the list based on the y co-ordinate and calculate the distances taking the subsequent 7 points
#     strips = mergeSortYcoordinate(strips)
#     strip_len = len(strips)
#     #print("length of strip = ", strip_len)
#     best_min = min_distance
#     #p1 = strips[0]
#     #p2 = strips[1]
#     for i in range(strip_len -1):
#         for j in range(i+1, min(strip_len,i+7)):
#             distance = distance_squared(strips[i],strips[j])
#             if distance < best_min:
#                 best_min = distance
#                 #p1 = strips[i]
#                 #p2 = strips[j]
#     return best_min


# def closestStripPair(points, min_distance):
#
#
#     mid = len(points) // 2
#     mid_x = points[mid].x               ## x co-ordinate of the mid point
#
#
#     ## scans the points and places in the strips list based on the y co-ordinate value
#     strips = []
#     for i in range(len(points)):
#         if points[i].x <= mid_x + min_distance and points[i].x >= mid_x - min_distance:
#             strips.append(points[i])
#             curr = len(strips) - 2
#             tmp = points[i]
#             tmp_y = points[i].y
#             if tmp.y < strips[curr].y and len(strips) > 1:              ## check and places the point in the list based on the y-value
#                 while (strips[curr].y > tmp.y) and curr >= 0:
#                     strips[curr+1] = strips[curr]
#                     curr -= 1
#                 strips[curr + 1] = tmp
#
#     strip_len = len(strips)
#     #print("length of strip = ", strip_len)
#     best_min = min_distance
#     #p1 = strips[0]
#     #p2 = strips[1]
#     for i in range(strip_len -1):
#         for j in range(i+1, min(strip_len,i+7)):
#             distance = distance_squared(strips[i],strips[j])
#             if distance < best_min:
#                 best_min = distance
#                 #p1 = strips[i]
#                 #p2 = strips[j]
#     return best_min


def closestStripPair(leftHalf, rightHalf, min_distance):
    total = leftHalf + rightHalf
    mid = len(total) // 2
    mid_x = total[mid].x               ## x co-ordinate of the mid point

    # make a list of the points which are min_distances apart from the x co-ordinate of the mid point
    strips = [point for point in total if mid_x - min_distance <= point.x <= mid_x + min_distance ]

    # sort the list based on the y co-ordinate and calculate the distances taking the subsequent 7 points
    #strips = mergeSortYcoordinate(strips)

    strips = sorted(strips, key = lambda point: point.y)

    strip_len = len(strips)
    #print("length of strip = ", strip_len)
    best_min = min_distance
    for i in range(strip_len -1):
        for j in range(i+1, min(strip_len,i+8)):
            distance = distance_squared(strips[i],strips[j])
            best_min = min(best_min, distance)
    return best_min



#print(closestStripPair([Point(5,2), Point(3,5), Point(1,0), Point(6,4), Point(10,10)], 5))
#print(bruteForce([Point(0, 2), Point(3, 5), Point(5,2)]))



def minimum_distance_squared_helper(points_sorted_x):

    #print("The list is ", points_sorted_x)
    points_length = len(points_sorted_x)
    if points_length <= 3:                        ## base condition for the recursive call
        return bruteForce(points_sorted_x)

    midIndex = points_length // 2          ## find the midpoint to split the points list into two halves
    leftHalf = points_sorted_x[:midIndex]
    rightHalf = points_sorted_x[midIndex:]

    ## call recursively to get the minimum distances for each split
    distance_1 = minimum_distance_squared(leftHalf)
    distance_2 = minimum_distance_squared(rightHalf)

    #print ("    Distance 1 = {}  Distance 2 = {} ". format(distance_1, distance_2))
    min_distance = min(distance_1, distance_2)
    #print("    The min distance = ", min_distance)

    ## the key thing to note is here is to recussively pass the left half and the right half.
    min_distance_stripe = closestStripPair(leftHalf,rightHalf,min_distance)

    #print("   After running the closestStripPair function distance = ", min_distance_stripe)
    best_distance = min(min_distance_stripe, min_distance)
    return best_distance


def minimum_distance_squared(points):
    points_sorted_x = sorted(points, key = lambda point: point.x)         # Presorting x-wise
    output = minimum_distance_squared_helper(points_sorted_x)
    return output

#print(minimum_distance_squared([Point(0, 2), Point(3, 5), Point(5,2), Point(1,0), Point(6,4), Point(10,10), Point(15,10), Point(20,15)]))



if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
