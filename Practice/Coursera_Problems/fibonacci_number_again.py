
def fibonacci_number(n):
    if n <= 1:
        return n
    f = [0] * (n+1)
    f[0], f[1] = 0, 1
    for i in range(2, len(f)):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def pisano_period(m):
    m_lst = []
    m_lst.append(0)
    m_lst.append(1)
    previous, current = 0, 1
    while not ((m_lst[previous] == 0 and m_lst[current] == 1) and (previous > 0)):
        previous, current = current, current+1
        m_lst.append((m_lst[current-1] + m_lst[current-2])%m)
    #return m_lst, current-1
    return current-1

def fibonacci_modulo(n, m):
    remainder = n % pisano_period(m)
    output = fibonacci_number(remainder) % m
    return output

#print(pisano_period(3))
#print(fibonacci_number(10))


if __name__ == '__main__':
    n,m = map(int, input().split())
    print(fibonacci_modulo(n,m))