# python3
##  Submitted

def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def pisano_period(m):
    previous,current = 0,1
    for i in range(0,m*m):
        previous, current = current, (previous+current)%m

        if (previous == 0 and current == 1):
            return i+1

def fibonacci_number(n):

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


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    remainder = n % pisano_period(m)
    result = fibonacci_number(remainder) % m
    return result


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))


#print(fibonacci_number_again(2015,3))
