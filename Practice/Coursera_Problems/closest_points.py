
from collections import namedtuple
from itertools import combinations
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distanceSquared(point_1, point_2):
    distance = ((point_1.x - point_2.x)**2) + ((point_1.y - point_2.y)**2)
    return distance

def bruteForceDistance(points):
    min_distance = distanceSquared(points[0], points[1])
    length_points = len(points)
    if len(points) == 2:
        return min_distance

    for i in range(length_points-1):
        for j in range(i+1, length_points):
            if i != 0 or j != 1:
                distance = distanceSquared(points[i], points[j])
                min_distance = min(distance, min_distance)
    return min_distance


def closestStripDistance(leftHalf, rightHalf, min_distance):
    total = leftHalf + rightHalf
    mid = len(total) //2

    mid_point_x = total[mid].x

    stripe = [ point for point in points if  mid_point_x - min_distance <= point.x <= mid_point_x + min_distance]

    stripe = sorted(stripe, key = lambda point:point.y)

    stripe_len = len(stripe)
    stripe_min = min_distance
    for i in range(stripe_len-1):
        for j in range(i+1, min(stripe_len, 8)):
            distance = distanceSquared(stripe[i], stripe[j])
            stripe_min = min(distance, stripe_min)
    return stripe_min


def closestPointsDistanceHelper(points):

    if len(points) <= 3:
        return bruteForceDistance(points)

    mid = len(points)//2
    leftHalf = points[:mid]
    rightHalf = points[mid:]

    distance_left = closestPointsDistanceHelper(leftHalf)
    distance_right = closestPointsDistanceHelper(rightHalf)

    min_distance_left_right = min(distance_left, distance_right)

    min_distance_stripe = closestStripDistance(leftHalf, rightHalf, min_distance_left_right)

    best_min_distance = min(min_distance_left_right, min_distance_stripe)

    return best_min_distance

def closestPointsDistance(points):
    points = sorted(points, key = lambda point:point.x)
    best_min_distance = closestPointsDistanceHelper(points)
    return best_min_distance


if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x,y = map(int, input().split())
        point = Point(x,y)
        points.append(point)
    shortest_distance = closestPointsDistance(points)
    print(sqrt(shortest_distance))