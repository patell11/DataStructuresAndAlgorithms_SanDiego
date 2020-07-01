# python3
import sys

'''
This function returns the list with the number of the operations required to obtain the value i.e the indices from 0 to n+1

'''

def min_ops(n):
    result = [0] * (n+1)
    for i in range(2, n+1):      # Starting from the index 2 as the operations required for the indices 0 and 1 is 0
        min_1 = result[i-1]
        min_2 = sys.maxsize
        min_3 = sys.maxsize

        if i % 2 == 0:
            min_2 = result[int(i/2)]
        if i % 3 == 0:
            min_3 = result[int(i/3)]
        min_ops = min(min_1, min_2, min_3)
        result[i] = min_ops + 1
    return result


'''
This function back track the list from the above function that has the number of operations for a given number - n.
It scans the list and reduces the value by -1, /3, /2
The key thing to note here is that if n is divisible is by only 2 or by only 3, in that case choose the n value comparing the minimum operations
between n-1 and n//2 or (n//3)
'''

def constructSequence(result, n):
    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n-1
        elif n % 2 == 0 and n % 3 == 0:
            n = n//3
        elif n % 2 == 0:
            if result[n-1] < result[n//2]:
                n = n-1
            else:
                n = n//2
        elif n % 3 == 0:
            if result[n-1] < result[n//3]:
                n = n-1
            else:
                n = n//3
    sequence = list(reversed(sequence))
    return sequence



def compute_operations(n):
    assert 1 <= n <= 10 ** 6

    if n == 1:
        return [1]

    ops_result = min_ops(n)
    return constructSequence(ops_result, n)

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

# input = sys.stdin.read()
# n = int(input)
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')