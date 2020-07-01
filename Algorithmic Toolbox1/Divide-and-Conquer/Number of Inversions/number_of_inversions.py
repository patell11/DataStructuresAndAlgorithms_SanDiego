# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(alist, n_inversions):


    if len(alist)>1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        compute_inversions(left, n_inversions)
        compute_inversions(right, n_inversions)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                alist[k] = left[i]
                i += 1
                k += 1
            else:
                # count the number of inversions by comparing the right element with the left element. If the right
                # element is smaller than the left then it's smaller than the all the elements in the left from the
                # position i therefore (len(left) -i)
                n_inversions[0] = n_inversions[0] + (len(left) - i)
                alist[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

    return n_inversions

#print(compute_inversions_naive([54,26,93,17,77,31,44,55,20]))

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    n_inversions = [0]
    result = compute_inversions(elements, n_inversions)
    print(*result)
