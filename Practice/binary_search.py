
def binarySearch(lst, item):
    start = 0
    end = len(lst)

    while start <= end:
        mid = (start + end)//2
        if lst[mid] == item:
            return True
        else:
            if lst[mid] > item:
                end = mid - 1
            else:
                start = mid + 1
    return False
#
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 13))

## Binary Search using the recursion

def binarySearchRec(lst, item):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst)//2
        if lst[mid] == item:
            return True
        elif lst[mid] > item:
            return binarySearchRec(lst[:mid], item)
        else:
            return binarySearchRec(lst[mid+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearchRec(testlist, 3))
print(binarySearchRec(testlist, 13))