
def isHeap(alist, index, size):

    if index > (size -2)/2:
        return True

    return (alist[index] >= alist[2*index+1] and
            alist[index] >= alist[2*index+2] and
            isHeap(alist, 2*index+1, size) and
            isHeap(alist, 2*index+2, size))

    return False

arr = [90, 15, 10, 7, 12, 2, 7, 3]
print(isHeap(arr, 0, len(arr)-1))