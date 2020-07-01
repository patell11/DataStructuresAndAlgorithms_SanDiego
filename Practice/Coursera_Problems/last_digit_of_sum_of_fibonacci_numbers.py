
def fib_units_60():
    fib_units_lst = [0] * 61
    fib_units_lst[0] = 0
    fib_units_lst[1] = 1
    for i in range(2, len(fib_units_lst)):
        fib_units_lst[i] = (fib_units_lst[i-1] + fib_units_lst[i-2])%10
    return fib_units_lst


def last_digit_sum_fibonacci(n):
    fib_units_60_lst = fib_units_60()
    lookup_length = n % 60
    sum_ = 0
    for i in range(lookup_length+1):
        sum_ = sum_ + fib_units_60_lst[i]
    return sum_ % 10


#print(fib_units_60())
if __name__ == '__main__':
    n = int(input())
    print(last_digit_sum_fibonacci(n))