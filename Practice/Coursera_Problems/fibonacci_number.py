
def fibonacci_number(number):
    n = number
    if number == 0:
        return 0
    if number <= 2:
        return 1
    else:
        numbers = [1] * (number +1)
        numbers[0] = 0
        i = 2
        while number >= 2:
            numbers[i] = numbers[i-1] + numbers[i-2]
            number -= 1
            i += 1
        return numbers[n]



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_number(n))