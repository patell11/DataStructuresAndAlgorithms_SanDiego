## Sorting algorithms v2 (practice)

def bubbleSort(lst):
    for i in range(len(lst)-2):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
    return lst

#print(bubbleSort([54,26,93,17,77,31,44,55,20]))

def shortBubbleSort(lst):
    changes = True
    iteration = 0
    i = 0
    while i < len(lst)-2 and changes:
        iteration += 1
        changes = False
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
                changes = True
    #print(iteration)
    return (lst, iteration)

#print(shortBubbleSort([16,14,5,6,8]))

def selectionSort(lst):
    for i in range(len(lst)-2):
        min = i
        for j in range(i,len(lst)):
            if lst[j] < lst[min]:
                min = j
        if i != j:
            tmp = lst[i]
            lst[i] = lst[min]
            lst[min] = tmp
    return lst

#print(selectionSort([54,26,93,17,77,31,44,55,20]))

def insertionSort(lst):
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i-1
        while (j >= 0 and lst[j] > tmp):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = tmp
    return lst

#print(insertionSort([7,4,10,8,3,1]))

def shellSort(lst):
    gap = int(len(lst)/2)
    while gap > 0:
        for i in range(gap, len(lst)):
            tmp = lst[i]
            j = i
            while (j>= gap and lst[j-gap] > tmp):
                lst[j] = lst[j-gap]
                j -= gap
            lst[j] = tmp
        gap = int(gap/2)
    return lst

#print(shellSort([23,29,15,19,31,7,9,5,2]))

def mergeSort(lst):
    if len(lst) > 1:
        mid = int(len(lst)/2)
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k] = lefthalf[i]
                k += 1
                i += 1
            else:
                lst[k] = righthalf[j]
                k += 1
                j += 1
        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            lst[k] = righthalf[j]
            j += 1
            k += 1
    return lst

print(mergeSort([23,29,15,19,31,7,9,5,2]))