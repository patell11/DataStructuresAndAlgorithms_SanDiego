

def car_fueling(distance, tank_capacity, stations):

    fuel_capacity = tank_capacity
    stations_fueled_at = []
    stations = [0] + stations + [distance]
    current = 0
    while stations[current] != distance:
        if stations[current] <= fuel_capacity and stations[current+1] <= fuel_capacity:
            current = current+1
        elif (stations[current] <= fuel_capacity) and (stations[current+1] > stations[current] + tank_capacity):
            return -1
        else:
            fuel_capacity = stations[current] + tank_capacity
            stations_fueled_at.append(stations[current])
    return stations_fueled_at


if __name__ == '__main__':
    distance = int(input())
    tank_capacity = int(input())
    n = int(input())
    stations = list(map(int, input().split()))
    print(car_fueling(distance, tank_capacity, stations))