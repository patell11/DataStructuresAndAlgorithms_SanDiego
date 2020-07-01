
from random import randint

def quickSort(alist, l, r):
    if l >= r:
        return
    ## pick any random index between the left and right and swap the element
    random_i = randint(l, r-1)
    alist[l], alist[random_i] = alist[random_i], alist[l]

    m1, m2 = partition3(alist, l, r)
    quickSort(alist, l, m1)
    quickSort(alist, m2+1, r)

    return alist

def partition3(alist, l, r):
    pivot = alist[l]
    j = l
    k = l
    for i in range(l+1, r):
        if alist[i] <= pivot:
            j = j+1
            alist[j], alist[i] = alist[i], alist[j]
        ## if the swapped element above is less than the pivot we move to the other end of the segment of m1--m2
            if alist[j] < pivot:
                k = k+1
                alist[k], alist[j] = alist[j], alist[k]
        #print("---", alist, k, j)
    #print("---", alist, k, j)
    if k == l:
        alist[j], alist[l] = alist[l], alist[j]
        m1, m2 = j, j
        #print("----> ", alist)
        return m1, m2
    else:
        alist[k], alist[l] = alist[l], alist[k]
        m1, m2 = k, j
        #print("----> ", alist)
        return m1, m2

if __name__=='__main__':
    n = int(input())
    alist = list(map(int, input().split()))
    assert len(alist) == n
    quickSort(alist, 0, len(alist))
    print(*alist)


