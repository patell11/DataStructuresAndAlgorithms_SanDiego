

def fib_units_60():
    fib_units_lst = [0] * 61
    fib_units_lst[0] = 0
    fib_units_lst[1] = 1
    for i in range(2, len(fib_units_lst)):
        fib_units_lst[i] = (fib_units_lst[i-1] + fib_units_lst[i-2])%10
    return fib_units_lst

def sum_fibonacci_numbers_interval(from_, to_):
    fib_units_lst = fib_units_60()
    from_lookup_length = from_ % 60
    to_lookup_length = to_ % 60

    sum_from_lookup_length = sum(fib_units_lst[0:from_lookup_length+1])
    sum_to_lookup_length = sum(fib_units_lst[0:to_lookup_length+1])

    if from_lookup_length <= to_lookup_length:
        return sum(fib_units_lst[from_lookup_length:to_lookup_length+1])%10
    else:
        if (sum_to_lookup_length % 10) < (sum_from_lookup_length % 10):
             return ((sum_to_lookup_length % 10) + 10) - (sum_from_lookup_length % 10)
        else:
            return (sum_to_lookup_length % 10) - (sum_from_lookup_length % 10)


if __name__ == '__main__':
    from_, to_ = map(int, input().split())
    print(sum_fibonacci_numbers_interval(from_, to_))