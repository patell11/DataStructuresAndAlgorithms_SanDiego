

def lcs2(sequence_1, sequence_2, len_1, len_2):

    rows = len_2 +1
    columns = len_1 +1

    length_matrix = [[None for column in range(columns)] for row in range(rows)]

    for column in range(columns):
        length_matrix[0][column] = 0
    for row in range(rows):
        length_matrix[row][0] = 0

    for row in range(1,rows):
        for column in range(1,columns):
            if sequence_1[column-1] == sequence_2[row-1]:
                length_matrix[row][column] = (length_matrix[row-1][column-1]) + 1
            else:
                length_matrix[row][column] = max(length_matrix[row][column-1], length_matrix[row-1][column])

    return length_matrix[rows-1][columns-1]

if __name__ == '__main__':
    len_1 = int(input())
    sequence_1 = list(map(int, input().split()))
    len_2 = int(input())
    sequence_2 = list(map(int, input().split()))
    print(lcs2(sequence_1, sequence_2, len_1, len_2))