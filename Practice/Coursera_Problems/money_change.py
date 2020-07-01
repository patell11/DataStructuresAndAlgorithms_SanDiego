

def number_of_coins(n):
    denominations = [1, 5, 10]
    num_coins = 0
    while n != 0:
        if n >= denominations[2]:
            num_coins = num_coins + (n // denominations[2])
            n = n % denominations[2]
        elif n >= denominations[1]:
            num_coins = num_coins + (n // denominations[1])
            n = n % denominations[1]
        else:
            num_coins = num_coins + n
            n = 0
    return num_coins



if __name__ == '__main__':
    n = int(input())
    print(number_of_coins(n))