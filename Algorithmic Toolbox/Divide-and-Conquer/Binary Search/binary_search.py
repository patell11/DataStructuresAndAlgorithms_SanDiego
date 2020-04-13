# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1

def binary_search_helper(lst, value):
    output = []
    for i in range(len(value))
    minIndex = 0
    maxIndex = len(lst)-1
    while maxIndex >= minIndex:
        mid = int((minIndex + maxIndex)/2)
        if lst[mid] == value:
            return mid
        elif lst[mid] > value:
            maxIndex = mid -1
        else:
            minIndex mid +1



def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    keys.sort()
    output = []
    for i in range(len(query)):
        minIndex = 0
        maxIndex = len(keys) - 1
        value = query[i]
        while maxIndex >= minIndex:
            mid = int((minIndex + maxIndex) / 2)
            if keys[mid] == value:
                output.append(mid)
            elif keys[mid] > value:
                maxIndex = mid - 1
            elif key[mid] < value:
                minIndex = mid + 1
            else:
                output.append(-1)
    return


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
