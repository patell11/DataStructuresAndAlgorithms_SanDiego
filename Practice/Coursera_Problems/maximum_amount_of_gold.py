

def maximum_gold(capacity, weights):

    weights_length = len(weights)
    weights_matrix = [[0 for c in range(capacity+1)] for weight in range(weights_length+1)]

    for row in range(weights_length+1):
        for column in range(capacity+1):
            if (row == 0 or column == 0):
                weights_matrix[row][column] = 0
            elif weights[row-1] <= column:
                weights_matrix[row][column] = max(weights[row-1] + weights_matrix[row-1][column-weights[row-1]], weights_matrix[row-1][column])
            else:
                weights_matrix[row][column] = weights_matrix[row-1][column]

    return weights_matrix[weights_length][capacity]

if __name__ == '__main__':
    capacity, n_bars = map(int, input().split())
    weights = list(map(int, input().split()))

    print(maximum_gold(capacity, weights))