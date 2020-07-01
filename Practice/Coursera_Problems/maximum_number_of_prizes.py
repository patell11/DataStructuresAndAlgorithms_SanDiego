

def maximum_num_prizes_naive(n):
    summands = []

    for i in range(1, n+1):
        summands.append(i)
        remaining = n - sum(summands)
        if sum(summands) > n or (remaining in summands):
            summands.pop()
    return summands

def maximum_num_prizes(n):
    summands = []

    num = n
    l = 1
    while num > 0:
        if num <= 2*l:
            summands.append(num)
            num -= num
            l += 1
        else:
            summands.append(l)
            num -= l
            l += 1
    return summands


if __name__ == '__main__':
    n = int(input())
    output = maximum_num_prizes(n)
    print(len(output))
    print(*output)

