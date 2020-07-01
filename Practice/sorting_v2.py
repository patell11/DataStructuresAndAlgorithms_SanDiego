## Sorting algorithms v2 (practice)

# def bubbleSort(lst):
#     for i in range(len(lst)-2):
#         for j in range(len(lst)-1-i):
#             if lst[j] > lst[j+1]:
#                 tmp = lst[j]
#                 lst[j] = lst[j+1]
#                 lst[j+1] = tmp
#     return lst

def bubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j+1] < lst[j]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst

print(bubbleSort([54,26,93,17,77,31,44,55,20]))

def shortBubbleSort(lst):
    exchanges = True
    for i in range(len(lst)-1):
        if exchanges:
            exchanges = False
            for j in range(len(lst)-i-1):
                if lst[j+1] < lst[j]:
                    exchanges = True
                    lst[j+1], lst[j] = lst[j], lst[j+1]
        else:
            print("No exchanges")
            break
    return lst

print(shortBubbleSort([8,12,48,89,96,219]))

# def selectionSort(lst):
#     for i in range(len(lst)-2):
#         min = i
#         for j in range(i,len(lst)):
#             if lst[j] < lst[min]:
#                 min = j
#         if i != j:
#             tmp = lst[i]
#             lst[i] = lst[min]
#             lst[min] = tmp
#     return lst

def selectionSort(lst):
    for i in range(len(lst)-1):
        max_ = -1
        max_index = -1
        for j in range(len(lst)-i):
            if lst[j] > max_:
                max_ = lst[j]
                max_index = j
        if max_index != -1:
            lst[max_index] = lst[len(lst)-i-1]
            lst[len(lst) - i - 1] = max_
    return lst

print(selectionSort([54,26,93,17,77,31,44,55,20]))

# def insertionSort(lst):
#     for i in range(1, len(lst)):
#         tmp = lst[i]
#         j = i-1
#         while (j >= 0 and lst[j] > tmp):
#             lst[j+1] = lst[j]
#             j -= 1
#         lst[j+1] = tmp
#     return lst

def insertionSort(lst):
    for i in range(1, len(lst)):
        ith_value = lst[i]
        index_ = i
        while index_ > 0 and lst[index_ - 1] > ith_value:
            lst[index_] = lst[index_ - 1]
            index_ -= 1
        lst[index_] = ith_value
        print("---",lst)
    return lst

print(insertionSort([7,4,10,8,3,1]))

# def shellSort(lst):
#     gap = int(len(lst)/2)
#     while gap > 0:
#         for i in range(gap, len(lst)):
#             tmp = lst[i]
#             j = i
#             while (j>= gap and lst[j-gap] > tmp):
#                 lst[j] = lst[j-gap]
#                 j -= gap
#             lst[j] = tmp
#         gap = int(gap/2)
#     return lst


def shellSort(lst):
    gap = len(lst)//2
    while gap > 0:
        for i in range(gap, len(lst)):
            ith_value = lst[i]
            index_ = i
            while index_ > 0 and lst[index_ - gap] > ith_value:
                lst[index_] = lst[index_ - gap]
                index_ = index_ - gap
            lst[index_] = ith_value
        gap = gap//2
    return lst
print(shellSort([23,29,15,19,31,7,9,5,2]))

def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        mergeSort(left)
        mergeSort(right)

        li = 0
        rj = 0
        lk = 0

        while li < len(left) and rj < len(right):
            if left[li] < right[rj]:
                lst[lk] = left[li]
                li += 1
                lk += 1
            else:
                lst[lk] = right[rj]
                rj += 1
                lk += 1

        while li < len(left):
            lst[lk] = left[li]
            li += 1
            lk += 1

        while rj < len(right):
            lst[lk] = right[rj]
            rj += 1
            lk += 1

    return lst


print("Merge Sort")
print(mergeSort([23,29,15,19,31,7,9,5,2]))

def quickSort(lst, start, end):
    if start >= end:
        return
    print("----", lst)
    partition_index = partition(lst, start, end)
    quickSort(lst, start, partition_index)
    quickSort(lst, partition_index+1, end)

    return lst

def partition(lst, start, end):
    pivot = lst[start]
    j = start
    for i in range(start+1, end):
        if lst[i] <= pivot:
            j += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[j], lst[start] = lst[start], lst[j]
    return j

print("Quick Sort")
lst = [23,29,15,19,31,7,9,5,2]
print(quickSort(lst, 0, len(lst)))

