

def buildHeap(n_input, alist, swap_indices):
    start_index = (len(alist)-2)//2
    while start_index >= 0:
        shiftDown(alist, start_index, swap_indices, n_input)
        start_index -= 1
    return swap_indices

def shiftDown(alist, index, swap_indices, size):
    min_index = index
    leftchild = 2*index + 1
    rightchild = 2*index + 2

    if leftchild < size and alist[min_index] > alist[leftchild]:
        min_index = leftchild
    if rightchild < size and alist[min_index] > alist[rightchild]:
        min_index = rightchild
    if min_index != index:
        swap_indices.append((index, min_index))
        alist[min_index], alist[index] = alist[index], alist[min_index]
        shiftDown(alist, min_index, swap_indices, size)


if __name__ == '__main__':
    n_input = int(input())
    a_list = list(map(int, input().split()))
    swap_indices = []
    print(buildHeap(n_input, a_list, swap_indices))