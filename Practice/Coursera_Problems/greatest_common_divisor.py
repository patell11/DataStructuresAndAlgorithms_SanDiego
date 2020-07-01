
def gcd(a,b):

    while b>0:
        rem = a%b
        a = b
        b = rem
    return a


if __name__ == '__main__':
    a,b = map(int, input().split())
    print(gcd(a, b))

