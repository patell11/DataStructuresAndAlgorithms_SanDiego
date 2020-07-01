

def fractional_knapsack(bag_capacity, value, weight, value_weight_ratio):
    max_value = []
    while bag_capacity > 0:
        index_max_ratio = value_weight_ratio.index(max(value_weight_ratio))
        if weight[index_max_ratio] > bag_capacity:
            selected_value = value_weight_ratio[index_max_ratio] * bag_capacity
            max_value.append(selected_value)
            value_weight_ratio[index_max_ratio] = 0
            bag_capacity = bag_capacity - weight[index_max_ratio]
        else:
            selected_value = value_weight_ratio[index_max_ratio] * weight[index_max_ratio]
            max_value.append(selected_value)
            value_weight_ratio[index_max_ratio] = 0
            bag_capacity = bag_capacity - weight[index_max_ratio]
    return sum(max_value)


if __name__ == '__main__':
    n, bag_capacity = map(int, input().split())
    value = []
    weight = []
    value_weight_ratio = []
    for i in range(n):
        v, w = map(int, input().split())
        value.append(v)
        weight.append(w)
        value_weight_ratio.append(v/w)
    result = fractional_knapsack(bag_capacity, value, weight, value_weight_ratio)
    print("{:.10f}".format(result))