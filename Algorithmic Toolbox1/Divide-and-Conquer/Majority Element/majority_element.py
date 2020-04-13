# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def chunk_process(lst_0, lst_1):
    lst = []
    for i in range(len(lst_1)):
        if lst_1[i] == lst_0[0]:
            lst_0.append(lst_1[i])
        else:
            lst.append(lst_1[i])
    return (lst_0, lst)


def count_merge(leftHalf,rightHalf):
    [left_major, left_minor] = chunk_process(leftHalf[0], leftHalf[1])
    [right_major, right_minor] = chunk_process(rightHalf[0], rightHalf[1])

    if left_major[0] == right_major[0]:
        return [left_major + right_major, left_minor + right_minor]
    elif len(left_major) > len(right_major):
        return [left_major, left_minor + right_major + right_minor]
    else:
        return [right_major, right_minor + left_minor + left_major]



def majority_element_helper(elements):
    elements_length = len(elements)
    if elements_length == 1:
        return [elements,[]]
    mid = elements_length // 2
    leftHalf = majority_element_helper(elements[:mid])
    rightHalf = majority_element_helper(elements[mid:])

    return count_merge(leftHalf,rightHalf)




def majority_element(elements):
    assert len(elements) <= 10 ** 5

    output_elements = majority_element_helper(elements)
    [major_lst, minor_lst] = chunk_process(output_elements[0], output_elements[1])
    if len(major_lst) > len(elements)/2:
        return 1
    else:
        return 0


#print(majority_element([5,2,2,2,5,5,5,5,2]))

# for elements in [
#     [7, 2, 7],
#     [7, 8, 9],
#     [2, 3, 2, 3],
#     [1, 2, 3, 4],
#
# ]:
#     print(
#         majority_element(list(elements)),
#         majority_element_naive(elements)
#     )

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
