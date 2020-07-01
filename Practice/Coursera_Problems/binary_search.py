
def binarySearchHelper(n, alist, k, blist):
    #print(k, blist)
    for i in range(len(blist)):
        #print("---",i)
        val = binarySearch(alist, blist[i])
        print(val, end = " ")
        #print("1")

def binarySearch(alist, item):
    left = 0
    right = len(alist)

    while left < right:
        mid = (left + right)//2
        if alist[mid] == item:
            return mid
        else:
            if alist[mid] > item:
                right = mid-1
            else:
                left = mid +1
    return -1

if __name__ == '__main__':
    first_line = list(map(int, input().split()))
    n = first_line[0]
    alist = first_line[1:]
    second_line = list(map(int, input().split()))
    k = second_line[0]
    blist = second_line[1:]
    binarySearchHelper(n,alist,k,blist)
