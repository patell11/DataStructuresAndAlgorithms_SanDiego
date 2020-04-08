# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]
        #print fibonacci_numbers
    return sum(fibonacci_numbers) % 10

## precomputing the units digit for the last 60 fibonacci numbers
def fib_units_60():
    f_lst = [0]*61
    f_lst[0] = 0
    f_lst[1] = 1
    for i in range(2,60+1):
        f_lst[i] = (f_lst[i-2] + f_lst[i-1])%10
    return f_lst



def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18



    f_lst = fib_units_60()
    lookup_len = n%60
    sum = 0
    for i in range(lookup_len+1):
        sum = sum + f_lst[i]
    return sum%10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))

# for n in range(20):
#     print(last_digit_of_the_sum_of_fibonacci_numbers(n),
#                      last_digit_of_the_sum_of_fibonacci_numbers_naive(n))

#613455


#print (last_digit_of_the_sum_of_fibonacci_numbers(100))
#print(last_digit_of_the_sum_of_fibonacci_numbers_naive(100))

