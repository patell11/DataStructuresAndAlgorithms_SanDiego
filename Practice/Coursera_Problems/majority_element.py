
def majority_element(alist, adict):

    if len(alist) == 1:
        if alist[0] in adict:
            adict[alist[0]] += 1
            return adict
        else:
            adict[alist[0]] = 1
            return adict

    if len(alist)>1:
        mid = len(alist)//2
        majority_element(alist[:mid], adict)
        majority_element(alist[mid:], adict)

    return adict


if __name__ == '__main__':
    n = int(input())
    alist = list(map(int, input().split()))
    adict = {}
    result_dict = majority_element(alist, adict)
    maximum = max(result_dict, key=result_dict.get)
    #print(maximum)
    if result_dict[maximum] > len(alist)//2:
        print(1)
    else:
        print(0)
