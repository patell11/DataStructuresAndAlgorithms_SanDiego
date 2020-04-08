# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


## precomputing the units digit for the last 60 fibonacci numbers
def fib_units_60():
    f_lst = [0]*61
    f_lst[0] = 0
    f_lst[1] = 1
    for i in range(2,60+1):
        f_lst[i] = (f_lst[i-2] + f_lst[i-1])%10
    return f_lst

def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18



    f_lst = fib_units_60()
    from_index = from_index % 60
    to_index = to_index % 60
    sum_to_index = sum(f_lst[0:to_index+1])
    sum_from_index = sum(f_lst[0:from_index])
    #print(sum_from_index, sum_to_index)
    if to_index >=  from_index:
        return sum(f_lst[from_index:to_index+1]) % 10
    else:
        if  sum_to_index % 10 == 0:
            val_sum_to_index = 0
        else:
            val_sum_to_index = (sum_to_index % 10) + 10
        val_sum_from_index = (sum_from_index % 10)
        return (val_sum_to_index - val_sum_from_index)
    #return sum(f_lst[from_index:to_index+1]) % 10
    #return (sum_to_index, sum_from_index)
    #print(from_index, to_index)
    #


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))

#
# for (from_index, to_index, last_digit) in [(3, 7, 1), (10, 10, 5), (100, 200, 0),
#                                            (17, 1700, 7),
#                                            (19, 10000000000, 1),(5618252, 6583591534156,6)]:
#     print(last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index), last_digit)


#print (last_digit_of_the_sum_of_fibonacci_numbers_again(5618252, 6583591534156))