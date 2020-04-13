# python3

from random import randint


def partition3(array, left, right):

    equal = left
    mid_2 = left
    pivot = array[left]
    # place the pivot element in the right position
    for i in range(left+1, right+1):
        if array[i] <= pivot:
            mid_2 = mid_2+1
            array[i], array[mid_2] = array[mid_2], array[i]

    array[left], array[mid_2] = array[mid_2], array[left]
    mid_1 = mid_2 - 1

    # After placing the pivot element its position iterate the array from the given indices
    # and check for the element same as the pivot element
    while equal != mid_1 and mid_1 > left and equal < mid_1:
        if array[equal] == array[mid_2]:
            # print("array[equal and array[end] ",(array[equal],array[end]))
            array[equal], array[mid_1] = array[mid_1], array[equal]
            mid_1 -= 1
        equal += 1

    # print("after loop end_prev = {}".format(end_prev))
    if mid_1 < 0:                        # if the end index is at the 0th position
        mid_1 = mid_1 +1

    # if there are no elements with the same value as the pivot, return both
    # the # mid1 and mid2 as the end
    if array[mid_1] != array[mid_2]:
        mid_1 = mid_2
    # print("m1 = {}, m2 = {}, output_array ={}".format(end_prev, end, array))
    # print("end value = ", end)
    # print("\n")
    return mid_1, mid_2



def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    # make a call to partition3 and then two recursive calls
    # to randomized_quick_sort

    (mid_1, mid_2) = partition3(array,left,right)
    randomized_quick_sort(array, left, mid_1-1)
    randomized_quick_sort(array, mid_2+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

# for array in [
#     ([1, 2, 3]),
#     ([3, 2, 1]),
#
# ]:
#     sorted_array = sorted(list(array))
#     randomized_quick_sort(array, 0, len(array) - 1)
#     print(array, sorted_array)
#
# lst = [2,3,9,2,9]
# randomized_quick_sort(lst, 0, len(lst)-1)
# print(lst)
# #print(partition3(lst,0,len(lst)-1))
