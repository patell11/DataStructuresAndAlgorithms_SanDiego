
def binarySearch(lst, item):
    first = 0
    last = len(lst)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if lst[midpoint] == item:
            found = True
        else:
            if lst[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

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
        else:
            if item < lst[mid]:
                return binarySearchRec(lst[:mid],item)
            else:
                return binarySearchRec(lst[mid+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearchRec(testlist, 3))
print(binarySearchRec(testlist, 10))