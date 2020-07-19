

def max_sliding_window(n_input, num_lst, window):
    index_queue = []
    result = []
    for i in range(window):
        while index_queue and num_lst[i] >= num_lst[index_queue[-1]]:
            index_queue.pop()
        index_queue.append(i)

    for i in range(window, n_input):

        result.append(num_lst[index_queue[0]])
        while index_queue and index_queue[0] <= i-window:
            index_queue.pop(0)

        while index_queue and num_lst[i] >= num_lst[index_queue[-1]]:
            index_queue.pop()
        index_queue.append(i)

    result.append(num_lst[index_queue[0]])
    return result

if __name__ == '__main__':
    n_input = int(input())
    num_lst = list(map(int, input().split()))
    window = int(input())
    print(max_sliding_window(n_input, num_lst, window))