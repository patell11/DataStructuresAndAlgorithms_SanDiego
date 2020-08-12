
if __name__ == '__main__':
    n_input = int(input())
    for i in range(n_input):
        len_list1, len_list2 = map(int, input().split())
        list1 = list(map(int, input().split()))
        list2 = list(map(int, input().split()))
        merge_list_using_shell_sort(list1, list2, len_list1, len_list2)