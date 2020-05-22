# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def max_sliding_window(sequence, m):
    window_size = m
    seq_len =  len(sequence)
    Qi = deque

    for i in range(window_size):
        while Qi and sequence[i] >= sequence[Qi[-1]]:
            Qi.pop()
        Qi.append(i)

    for i in range(window_size, seq_len):
        print(sequence[Qi[0]])

        while Qi and Qi[0] <= i-window_size:
            Qi.popleft()

        while Qi and sequence[i] >= sequence[Qi[-1]]:
            Qi.pop()

        Qi.append(i)
    print(sequence[Qi[0]])

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

