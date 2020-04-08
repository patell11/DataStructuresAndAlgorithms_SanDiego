# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


## precomputing the units digit for the last 60 fibonacci numbers
def fib_units_60():
    f_lst = [0]*61
    f_lst[0] = 0
    f_lst[1] = 1
    for i in range(2,60+1):
        f_lst[i] = (f_lst[i-2] + f_lst[i-1])%10
    return f_lst


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18


    f_lst = fib_units_60()
    f_lst_lookup_length = n%60
    f_lst = f_lst[0:f_lst_lookup_length+1]
    square_sum = sum(val**2 for val in f_lst)
    return square_sum % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))

# for n in range(20):
#     print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n),
#                      last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n))
#
# print ("\n")
#
# for (n, last_digit) in [(73, 1), (1234567890, 0)]:
#     print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n), last_digit)
#