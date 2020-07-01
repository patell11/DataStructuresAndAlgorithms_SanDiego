
def max_pairwise_product(numbers):
    max_index = 0
    for i in range(len(numbers)):
        if numbers[max_index] < numbers[i]:
            max_index = i

    second_max_index = 0
    for i in range(len(numbers)):
        if numbers[second_max_index] <= numbers[i] and i != max_index:
            second_max_index = i

    return numbers[max_index] * numbers[second_max_index]


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    assert n == len(numbers)
    print(max_pairwise_product(numbers))