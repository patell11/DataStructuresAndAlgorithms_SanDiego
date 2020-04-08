# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d


    numRefills = 0
    currentRefill = 0
    gas_stations = [0] + stops + [d]
    while (gas_stations[currentRefill] != d):
        lastRefill = currentRefill
        while(gas_stations[currentRefill] != d and (gas_stations[currentRefill + 1] - gas_stations[lastRefill] <= m)):
            currentRefill += 1
        if currentRefill == lastRefill:
            return -1
        elif (gas_stations[currentRefill] != d):
            numRefills += 1
    return numRefills

if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))

#
# for (d, m, stops, answer) in [
#     (950, 400, [200, 375, 550, 750], 2),
#     (10, 3, [1, 2, 5, 9], -1),
#     (200, 250, [100, 150], 0)
#
# ]:
#     print(compute_min_number_of_refills(d, m, stops), answer)
#