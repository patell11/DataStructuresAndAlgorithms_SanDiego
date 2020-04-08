# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)


    price_weight_ratio = [price * 1.0/weight for price,weight in zip(prices,weights) ]
    max_prices = []
    while capacity > 0:
        max_price_weight_ratio = max(price_weight_ratio)
        max_pwr_index = price_weight_ratio.index(max_price_weight_ratio)
        if weights[max_pwr_index] > capacity:
            price = capacity * max_price_weight_ratio
            max_prices = max_prices + [price]
            capacity = capacity - weights[max_pwr_index]
            price_weight_ratio[max_pwr_index] = 0
        elif weights[max_pwr_index] <= capacity:
            price = max_price_weight_ratio * weights[max_pwr_index]
            max_prices = max_prices + [price]
            price_weight_ratio[max_pwr_index] = 0
            capacity = capacity - weights[max_pwr_index]
    return round(sum(max_prices),3)






if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))

#
# for (capacity, weights, prices, answer) in [
#     (50, [20, 50, 30], [60, 100, 120], 180.0),
#     (10, [30], [500], 500 / 3),
#     (50,[20,50,30,40], [60,100,120,160],200)
#
# ]:
#     print(
#         maximum_loot_value(capacity, weights, prices),
#         answer
#     )
#