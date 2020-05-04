# python3

from itertools import product
from sys import stdin

## http://thisthread.blogspot.com/2018/02/2-partition-problem.html

#
# def partition3(values):
#     assert 1 <= len(values) <= 20
#     assert all(1 <= v <= 30 for v in values)
#
#
#     len_values = len(values)
#     lst_sum = sum(values)
#     rows = lst_sum//3
#     print(rows)
#     if lst_sum % 3 != 0:
#         return False
#
#     matrix = [[True for column in range(len_values+1)] for row in range(rows+1)]
#
#     for row in range(rows+1):
#         for column in range(len_values+1):
#             if row == 0:
#                 matrix[row][column] = True
#             elif (row != 0 and column == 0):
#                 matrix[row][column] = False
#             else:
#                 matrix[row][column] = matrix[row][column -1]
#                 if row >= values[column-1]:
#                     matrix[row][column] = (matrix[row][column] or matrix[row-values[column-1]][column-1])
#     return matrix
#
# # if __name__ == '__main__':
# #     input_n, *input_values = list(map(int, stdin.read().split()))
# #     assert input_n == len(input_values)
# #     print(partition3(input_values))


# print(partition3([1,2,3,6]))
# python3
import numpy

# Discrete Knapsack problem without repetition
def partitions3(W, n, items):
    """ Finds if number of partitions having capacity W is >=3
    (int, int, list) -> (int) """
    count = 0
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1

    if count < 3: print('0')
    else: print('1')

print(partitions3(8,9,[7, 2, 2, 2, 2, 2, 2, 2, 3]))

# if __name__ == '__main__':
#     n = int(input())
#     item_weights = [int(i) for i in input().split()]
#     total_weight = sum(item_weights)
#     if n<3:
#         print('0')
#     elif total_weight%3 != 0:
#         print('0')
#     else:
#         partitions3(total_weight//3, n, item_weights)
