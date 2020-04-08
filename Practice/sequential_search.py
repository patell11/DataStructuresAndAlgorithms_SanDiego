
def sequential_search(lst, item):
    found = False
    pos = 0
    stop = False
    while pos < len(lst) and not found and not stop:
        if lst[pos] == item:
            found = True
        else:
            if lst[pos] > item:
                found = True
            else:
                pos = pos + 1
    return found

lst = [1,2,3,4,5]
print(sequential_search(lst,6))

