# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45
    print("compute F sub", n)
    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n == 0:
        return 0
    if n <= 2:
        return 1
    else:
        f_list = [1] * n
        length = n
        i = 2
        while length > 2:
            f_list[i] = f_list[i-1] + f_list[i-2]
            length = length -1
            i = i+1
    return f_list[n-1]




if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

#print(fibonacci_number_naive(5))
#print(fibonacci_number(40))