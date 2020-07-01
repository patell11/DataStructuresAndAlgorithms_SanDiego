
def last_digit_fibonacci(n):
    if n <= 1:
        return n
    else:
        f = [0] * (n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2, len(f)):
            f[i] = (f[i-1] + f[i-2])%10
        return f[n]

if __name__ == '__main__':
    n = int(input())
    print(last_digit_fibonacci(n))
