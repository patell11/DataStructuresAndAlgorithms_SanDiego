

from itertools import permutations
from math import log


def largest_number(nums):
    max_num = ""
    while len(nums) > 0:
        value = nums[0]

        value_first_digit = int(str(value)[0])

        max_first_digit = value_first_digit
        for next_num in nums[1:]:
            next_num_first_digit = int(str(next_num)[0])

            if next_num_first_digit > max_first_digit:
                max_first_digit = next_num_first_digit
                value = next_num
            ## if the first digit is same then compare (a+b) and (b+a). eg 231 and 23 compare (23123 and 23231)
            elif next_num_first_digit == max_first_digit:
                if int(str(value) + str(next_num)) > int(str(next_num) + str(value)):
                    value = value
                else:
                    value = next_num
                    max_first_digit = next_num_first_digit
                #print("----",str(value) , str(next_num))

        max_num = max_num + str(value)
        #print(max_num)
        nums.remove(value)
    return max_num


# for numbers in [
#     [2, 21, 23, 211, 213, 231, 232],
# ]:
#     print(largest_number(numbers))




if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(largest_number(nums))
