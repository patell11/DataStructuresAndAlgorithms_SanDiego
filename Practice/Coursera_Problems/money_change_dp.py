

def minimum_num_coins(n):
    denominations = [1,3,4]
    rows = len(denominations)
    columns = n+1
    change_list = [columns] * columns
    change_list[0] = 0

    for row in range(rows):
        for column in range(columns):
            if column >= denominations[row]:
                if change_list[column] > change_list[column-denominations[row]]+1:
                    change_list[column] = change_list[column-denominations[row]] +1

    return change_list[n]


if __name__ == '__main__':
    n = int(input())
    print(minimum_num_coins(n))
