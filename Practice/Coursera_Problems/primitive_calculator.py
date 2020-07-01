
import sys

def minOps(n):
    num_ops = [0] * (n+1)
    for i in range(2, n+1):
        min_1 = num_ops[i-1]
        min_2 = sys.maxsize
        min_3 = sys.maxsize

        if i % 2 == 0:
            min_2 = num_ops[i//2]
        if i % 3 == 0:
            min_3 = num_ops[i//3]

        min_ops = min(min_1, min_2, min_3)
        num_ops[i] = min_ops + 1
    return num_ops

def constructSequenceHelper(num_ops, n):
    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n-1
        elif n % 2 == 0 and n % 3 == 0:
            n = n//3
        elif n % 2 == 0:
            if num_ops[n-1] < num_ops[n//2]:
                n = n-1
            else:
                n = n//2
        elif n % 3 == 0:
            if num_ops[n-1] < num_ops[n//3]:
                n = n -1
            else:
                n = n//3
    sequence= list(reversed(sequence))
    return sequence


def constructSequence(n):
    num_ops = minOps(n)
    sequence = constructSequenceHelper(num_ops, n)
    return sequence


if __name__ == '__main__':
    n = int(input())
    sequence = constructSequence(n)
    print(len(sequence)-1)
    print(*sequence)