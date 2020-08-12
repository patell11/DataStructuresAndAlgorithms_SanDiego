
from binary_heap import BinaryHeap

def merge_list_insertion(list1, list2, len_list1, len_list2):
    final_list = list1 + list2

    for i in range(len_list1, len(final_list)):
        key = final_list[i]
        prev = i -1

        while prev >= 0 and final_list[prev] > key:
            final_list[prev+1] = final_list[prev]
            prev -= 1

        final_list[prev+1] = key

    print(*final_list)
    return

def merge_list_merge(list1, list2, len_list1, len_list2):
    final_list = [None] * (len_list1 + len_list2)

    pos1 = 0
    pos2 = 0
    final_pos = 0

    while pos1 < len_list1 and pos2 < len_list2:
        if list1[pos1] < list2[pos2]:
            final_list[final_pos] = list1[pos1]
            pos1 += 1
            final_pos += 1
        else:
            final_list[final_pos] = list2[pos2]
            pos2 += 1
            final_pos += 1

    while pos1 < len_list1:
        final_list[final_pos] = list1[pos1]
        final_pos += 1
        pos1 += 1

    while pos2 < len_list2:
        final_list[final_pos] = list2[pos2]
        final_pos += 1
        pos2 += 1

    print(*final_list)
    return

def merge_list_using_heap(list1, list2, len_list1, len_list2):
    heap_instance = BinaryHeap()
    heap_instance.buildHeap(list2)
    for i in range(len_list1):
        if list1[i] > heap_instance.heaplist[0]:
            list1[i], heap_instance.heaplist[0] = heap_instance.heaplist[0], list1[i]
            heap_instance.shiftDown(0)
    heap_instance.inplace_sort()
    sorted_list = heap_instance.getHeap()
    sorted_list.reverse()
    print(list1 + sorted_list)
    return

def get_gap(gap):
    if gap <= 1:
        return 0
    return gap //2 + gap % 2

def merge_list_using_shell_sort(list1, list2, len_list1, len_list2):

    gap = get_gap(len_list1 + len_list2)

    while gap > 0:

        pos1 = 0
        while pos1 + gap < len_list1:
            if list1[pos1] > list1[pos1 + gap]:
                list1[pos1], list1[pos1 + gap] = list1[pos1 + gap], list1[pos1]
            pos1 += 1

        pos2 = gap - len_list1 if gap > len_list1 else 0
        while pos1 < len_list1 and pos2 < len_list2:
            if list2[pos2] < list1[pos1]:
                list2[pos2], list1[pos1] = list1[pos1], list2[pos2]
            pos1 += 1
            pos2 += 1

        if pos2 < len_list2:
            pos2 = 0
            while pos2 + gap < len_list2:
                if list2[pos2] > list2[pos2 + gap]:
                    list2[pos2], list2[pos2 + gap] = list2[pos2 + gap] + list2[pos2]
                pos2 += 1

        gap = get_gap(gap)

    print(*(list1 + list2))

if __name__ == '__main__':
    n_input = int(input())
    for i in range(n_input):
        len_list1, len_list2 = map(int, input().split())
        list1 = list(map(int, input().split()))
        list2 = list(map(int, input().split()))
        merge_list_using_shell_sort(list1, list2, len_list1, len_list2)