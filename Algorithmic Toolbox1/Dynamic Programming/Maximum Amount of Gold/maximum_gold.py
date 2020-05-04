# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)


    weights_len = len(weights)
    matrix = [[0 for c in range(capacity+1)] for weight in range(weights_len+1)]

    for row in range(weights_len+1):
        for column in range(capacity+1):
            if (row == 0 or column == 0):
                matrix[row][column] = 0
            elif weights[row-1] <= column:
                matrix[row][column] = max(weights[row-1] + matrix[row-1][column-weights[row-1]] , matrix[row-1][column])
            else:
                matrix[row][column] = matrix[row-1][column]
    return matrix[weights_len][capacity]



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
