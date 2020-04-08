
def bubbleSort(alist):
    for i in range(len(alist)-1):
        print("alist {} for i = {}".format(alist,i))
        for j in range(len(alist)-i-1):
            print("      alist {} for j = {}".format(alist, j))
            if alist[j] > alist[j+1]:
                tmp = alist[j+1]
                alist[j+1] = alist[j]
                alist[j] = tmp


#alist = [54,26,93,17,77,31,44,55,20]
#bubbleSort(alist)
#print(alist)


def selectionSort(alist):
    for i in range(len(alist)):
        print("alist {} for i = {}".format(alist, i))
        max_pos = 0
        for j in range(len(alist)-i):
            print("       alist[j] = {}, max_pos = {}".format(alist[j],max_pos))
            if alist[j] > alist[max_pos]:
                max_pos = j
                print("      max = {}".format(alist[max_pos]))
        tmp = alist[len(alist)-1-i]
        alist[len(alist)-1-i] = alist[max_pos]
        alist[max_pos] = tmp
        print("      alist {} for j = {}".format(alist, j))

# alist = [54,26,93,17,77,31,44,55,20]
# selectionSort(alist)
# print(alist)


def insertionSort(alist):
    for i in range(1, len(alist)):
        currentValue = alist[i]
        position = i
        while position > 0 and alist[position -1] > currentValue:
            alist[position] =  alist[position -1]
            position = position - 1
        alist[position] = currentValue

# alist = [54,26,93,17,77,31,44,55,20]
# insertionSort(alist)
# print(alist)


def shellSort(alist):
    gap = len(alist)//2
    while gap > 0:
        for i in range(gap,len(alist)):
            tmp = alist[i]
            j = i
            while j >= gap and alist[j-gap] > tmp:
                alist[j] = alist[j-gap]
                j = j-gap
            alist[j] = tmp
        gap = gap//2


# alist = [54,26,93,17,77,31,44,55,20]
# shellSort(alist)
# print(alist)


def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
                k = k+1
            else:
                alist[k] = righthalf[j]
                j = j+1
                k = k+1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    print("Merging ", alist)

# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        pivot_pos = partition(alist, first, last)
        quickSortHelper(alist,first, pivot_pos-1)
        quickSortHelper(alist,pivot_pos+1, last)

def partition(alist, first, last):
    pivot = alist[first]
    start = first
    end = last

    while (start < end):

        while(alist[start] <= pivot):
            start = start +1
        while(alist[end] > pivot ):
            end = end -1
        if(start < end):
            tmp = alist[end]
            alist[end] = alist[start]
            alist[start] = tmp

    tmp = alist[end]
    alist[end] = alist[first]
    alist[first] = tmp

    return end

alist = [54,26,93,17,77,31,44,55,20]
quickSort   (alist)
print(alist)