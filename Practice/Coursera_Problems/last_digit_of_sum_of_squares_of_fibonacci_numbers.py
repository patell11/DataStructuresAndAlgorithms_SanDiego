

def fib_units_60():
    f = [0]*(60+1)
    f[1] = 1
    for i in range(2, len(f)):
        f[i] = (f[i-1] + f[i-2])%10
    return f

def last_digit_sum_square_fibonacci(n):
    fib_units_lst = fib_units_60()
    lookup_length = n % 60

    f_lst = fib_units_lst[0:lookup_length+1]
    square_sum = sum(val ** 2 for val in f_lst)

    return square_sum % 10

if __name__ == '__main__':
    n = int(input())
    print(last_digit_sum_square_fibonacci(n))