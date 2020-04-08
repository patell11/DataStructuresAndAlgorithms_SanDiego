# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n
    else:
        fib = [0] * (n+1)
        fib[0] = 0
        fib[1] = 1
        for i in range(2,n+1):
            fib[i] = (fib[i-2] + fib[i-1])%10
        return fib[n]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))

#print(last_digit_of_fibonacci_number(91239))