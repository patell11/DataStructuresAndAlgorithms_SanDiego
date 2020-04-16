# python3
import sys


# A naive recursive approach
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0;
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1);
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n));



def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    # if len(second_sequence) == 1:
    #     if second_sequence in first_sequence:
    #         return 1
    #     else:
    #         return 0

    rows = len(second_sequence) + 1
    columns = len(first_sequence) + 1
    sequence_matrix = [[None for column in range(columns)] for row in range(rows)]

    for row in range(rows):
        sequence_matrix[row][0] = 0
    for column in range(columns):
        sequence_matrix[0][column] = 0

    max_seq_length = 0
    for row in range(1, rows):
        for column in range(1, columns):
            if first_sequence[column-1] == second_sequence[row-1]:
                sequence_matrix[row][column] = (sequence_matrix[row-1][column-1]) + 1
            else:
                sequence_matrix[row][column] = max(sequence_matrix[row-1][column], sequence_matrix[row][column-1])
            if sequence_matrix[row][column] > max_seq_length:
                max_seq_length = sequence_matrix[row][column]

    return sequence_matrix[rows-1][columns-1]

#print(lcs2([1,2,3],[3,2,1]))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
