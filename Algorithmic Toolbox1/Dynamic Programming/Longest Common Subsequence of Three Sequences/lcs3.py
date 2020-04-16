# python3


'''
This is the extension of the longest common subsequence of two sequences problem.

'''

def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100


    third = len(third_sequence) +1
    second = len(second_sequence) +1
    first = len(first_sequence) +1

    seq_matrix = [[[None for i in range(third)]
                    for j in range(second)]
                    for k in range(first)]

    for i in range(first):
        for j in range(second):
            for k in range(third):
                if (i == 0 or j == 0 or k == 0):
                    seq_matrix[i][j][k] = 0
                elif (first_sequence[i-1] == second_sequence[j-1] and first_sequence[i-1] == third_sequence[k-1]):
                    seq_matrix[i][j][k] = seq_matrix[i-1][j-1][k-1] + 1
                else:
                    seq_matrix[i][j][k] = max(max(seq_matrix[i-1][j][k], seq_matrix[i][j-1][k]), seq_matrix[i][j][k-1])
    return seq_matrix[first-1][second-1][third-1]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
