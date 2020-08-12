

def shell_sort(alist):

    len_alist = len(alist)
    gap = len_alist//2

    while gap > 0:

        for i in range(gap, len_alist):

            key = alist[i]
            curr = i
            while curr-gap >= 0 and alist[curr-gap] > key:
                alist[curr], alist[curr-gap] = alist[curr-gap], alist[curr]
                curr = curr - gap
        gap //= 2

alist = [12,34,54,2,3,19,13]
shell_sort(alist)
print(alist)

# if __name__ == '__main__':
#     alist = list(map(int, input().split()))
#     shell_sort(alist)
#     print(alist)