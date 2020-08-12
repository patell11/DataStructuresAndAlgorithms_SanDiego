# code
import sys


def count_triplets(n, lst):
    max_ele = 0

    for i in range(n):
        max_ele = max(max_ele, lst[i])
    print(max_ele)

    freq = [0] * (max_ele + 1)

    for i in range(n):
        freq[lst[i]] += 1

    triplet_count = 0
    triplet_count += (freq[0] * (freq[0] - 1) * (freq[0] - 2)) // 6

    for i in range(max_ele + 1):
        triplet_count += (freq[0] * freq[i] * (freq[i] - 1)) // 2

    for i in range(1, (max_ele + 1) // 2):
        triplet_count += (freq[i] * (freq[i] - 1) * freq[2 * i]) // 2

    for i in range(1, max_ele + 1):
        for j in range(i + 1, max_ele - i + 1):
            triplet_count += freq[i] * freq[j] * freq[i + j]

    if triplet_count != 0:
        print(triplet_count)
    else:
        print(-1)

    return


if __name__ == '__main__':
    n_input = int(input())
    for i in range(n_input):
        n = int(input())
        lst = list(map(int, input().split()))
        count_triplets(n, lst)
