# python3


def build_heap(alist):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    shifts the value down if its greater than its child value

    Follows the 0 based index
    """
    swaps = []
    size = len(alist)
    internal_nodes = (size -2)//2   # start to check the value from the last internal node
    while internal_nodes >= 0:
        shiftDown(internal_nodes, alist, swaps, size)
        internal_nodes = internal_nodes -1
    return swaps


def shiftUp(index, alist, swaps):
    i = index
    while i > 0:
        if alist[i] < alist[(i-1)//2]:
            alist[i], alist[(i-1)//2] = alist[(i-1)//2], alist[i]
            swaps.append(((i-1)//2, i))
        i = (i-1)//2



def shiftDown(index, alist, swaps, size):
    min_index = index
    leftchild = 2 * index + 1
    rightchild = 2 * index + 2

    if leftchild < size and alist[min_index] > alist[leftchild]:
        min_index = leftchild
    if rightchild < size and alist[min_index] > alist[rightchild]:
        min_index = rightchild
    if min_index != index:
        alist[min_index], alist[index] = alist[index], alist[min_index]
        swaps.append((index, min_index))
        shiftDown(min_index, alist, swaps, size)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
