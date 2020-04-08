# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    denominations = [1,5,10]
    n = money
    num_coins = 0
    while n != 0:
        if n >= denominations[2]:
            num_coins = num_coins + int(n / denominations[2])
            n = n % denominations[2]
        elif n >= denominations[1]:
            num_coins = num_coins + int(n/denominations[1])
            n = n % denominations[1]
        else:
            num_coins = num_coins + n
            n = 0
    return num_coins



if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))

# for (money, number_of_coins) in [(1, 1), (2, 2), (28, 6), (25,3), (40,4), (10,1), (5,1), (1000,100)]:
#     print(money_change(money), number_of_coins)
