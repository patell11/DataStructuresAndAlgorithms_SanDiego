# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

""" Create a Double Ended Queue, Qi that  
    will store indexes of array elements.  
    The queue will store indexes of useful  
    elements in every window and it will 
    maintain decreasing order of values from 
    front to rear in Qi, i.e., arr[Qi.front[]] 
    to arr[Qi.rear()] are sorted in decreasing 
    order"""

def max_sliding_window(sequence, m):
    window_size = m
    seq_len =  len(sequence)
    Qi = deque()
    result = []

    # Process first k (or first window) elements of array
    for i in range(window_size):
        # For every element, the previous smaller elements are useless so remove them from Qi
        while Qi and sequence[i] >= sequence[Qi[-1]]:
            Qi.pop()
        Qi.append(i)

    # Process rest of the elements, i.e. from arr[k] to arr[n-1]
    for i in range(window_size, seq_len):

        # The element at the front of the queue is the largest element of previous window, so print it
        result.append(sequence[Qi[0]])
        # Remove the elements which are out of this window
        while Qi and Qi[0] <= i-window_size:
            # remove from front of deque
            Qi.popleft()
        # Remove all elements smaller than the currently being added element (Remove useless elements)
        while Qi and sequence[i] >= sequence[Qi[-1]]:
            Qi.pop()

        Qi.append(i)
    # Print the maximum element of last window
    result.append(sequence[Qi[0]])
    return result

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

