# python3

from itertools import permutations
from math import log

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def get_first_digit(numbers):
    first_digits = [val // 10 ** (int(log(val, 10))) for val in numbers]
    return first_digits

def lst_to_int(numbers):
    value = ""
    for i in range(len(numbers)):
        value += str(numbers[i])
    return int(value)

#print(lst_to_int([15,23,99,9,6]))

def swap(lst, pos1, pos2):
    tmp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = tmp
    return lst

# numbers = [15,23,99,9,6]
# print(swap(numbers ,0, 2))



def largest_number(numbers):

    # numbers.sort(reverse = True)
    # first_digits = get_first_digit(numbers)
    # max_salary = ""
    # for i in range(len(first_digits)):
    #     max_index_first_digits = max(enumerate(first_digits),key=lambda x: x[1])[0]
    #     value = numbers[max_index_first_digits]
    #     first_digits[max_index_first_digits] = -1
    #     max_salary += str(value)
    #
    max_salary_lst = []
    for i in range(len(numbers)):
        max_salary_lst.append(numbers[i])
        max_num = lst_to_int(max_salary_lst)
        stop = True
        curr = len(max_salary_lst)-1
        prev = len(max_salary_lst)-1
        l = len(max_salary_lst)-2
        while(l >= 0 and stop):
            max_salary_lst = swap(max_salary_lst, l, l+1)
            new_max = lst_to_int(max_salary_lst)
            if new_max > max_num:
                max_num = new_max
            else:
                stop = False
                max_salary_lst = swap(max_salary_lst, l, l+1)
            l -= 1

    return  max_salary_lst #(lst_to_int(max_salary_lst))


#print(largest_number_naive([15,23,99,9,6]))
#print(largest_number([15,23,99,9,6]))


# if __name__ == '__main__':
#     n = int(input())
#     input_numbers = input().split()
#     assert len(input_numbers) == n
#     print(largest_number(input_numbers))

for numbers in [
    [1],
    [1, 2],

    [1, 12],
    [2, 12],
    [2, 21],
    [2, 21, 23, 211, 213, 231, 232]
]:
    print(largest_number(numbers),
                     largest_number_naive(numbers))

