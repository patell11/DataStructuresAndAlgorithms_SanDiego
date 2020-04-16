# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


'''
Maintain the denominations in sorted order. If the value of the column is greater than the denomination we are iterating for, 
value = 1 + the list value with index column - denomination value

'''

def change(money):

    denominations = [1,3,4]
    rows = len(denominations)
    size = money + 1
    change_lst = [money+1] * size               # Insert the value in the list with some large value
    change_lst[0] = 0

    for row in range(rows):
        for column in range(size):
            if column >= denominations[row]:
                if change_lst[column - denominations[row]] + 1 < change_lst[column]:
                    change_lst[column] = 1 + change_lst[column - denominations[row]]

    return change_lst[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))

#print(change(11))