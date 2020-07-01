

import sys

def num_edit_distance(str1, str2):
    if str1 == str2:
        return 0

    rows = len(str2)+1
    columns = len(str1) + 1

    distance_matrix = [[sys.maxsize for column in range(columns)] for row in range(rows)]

    for column in range(columns):
        distance_matrix[0][column] = column

    for row in range(rows):
        distance_matrix[row][column] = row

    for row in range(1,rows):
        for column in range(1,columns):
            if str1[column-1] == str2[row-1]:
                distance_matrix[row][column] = distance_matrix[row-1][column-1]
            else:
                distance_matrix[row][column] = min(distance_matrix[row][column-1],
                                                   distance_matrix[row-1][column],
                                                   distance_matrix[row-1][column-1]) + 1
    return distance_matrix[rows-1][columns-1]




if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(num_edit_distance(str1, str2))
