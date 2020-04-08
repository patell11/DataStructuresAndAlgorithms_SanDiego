# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

def segments_list(segments):
    lst = []
    for i in range(len(segments)):
        lst.append([segments[i].start, segments[i].end])
    lst.sort(key=lambda x:x[1])
    return lst

#print(segments_list([Segment(1, 3), Segment(2, 5), Segment(3, 6), Segment(1,2)]))


def compute_optimal_points(segments):
    #type here

    lst = segments_list(segments)
    #print("Sorted List:",lst )
    prev = 0
    num_count = 0
    output_lst = []
    while prev < len(segments):
        left = lst[prev][0]
        right = lst[prev][1]
        next = prev + 1
        change = False
        num_count = num_count + 1
        while ((next < len(segments)) and ( (lst[prev][0] >= lst[next][0] and lst[prev][0] <= lst[next][1]) or
                                            (lst[prev][1] >= lst[next][0] and lst[prev][1] <= lst[next][1]) )):
                ## The above condition is to check if the coordnate lies within the next corodinate

            #print ( "{} <= {} <= {}".format(lst[next][0] , lst[prev][0] ,lst[next][1]  ))
            #print("{} <= {} <= {}".format(lst[next][0] , lst[prev][1] ,lst[next][1] ))

            if (lst[prev][1] >= lst[next][0] and lst[prev][1] <= lst[next][1]):
                output = lst[prev][1]
            elif (lst[prev][0] >= lst[next][0] and lst[prev][0] <= lst[next][1]):
                output = lst[prev][0]

            next = next + 1
            change = True


        if change:
            prev = next
            output_lst.append(output)
        else:                                       ## If the condition does not fall in the while loop we need to change the prev vlaue
            output_lst.append(lst[prev][1])
            prev = prev + 1

    return output_lst


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    #print(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)

#
# for (segments, answer) in [
#     ([Segment(1, 3), Segment(2, 5), Segment(3, 6)], 1),
#     ([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)], 2),
#     ([Segment(41,42), Segment(52,52), Segment(63,63), Segment(80,82), Segment(78,79), Segment(35,35), Segment(22,23),
#      Segment(31,32), Segment(44,45), Segment(81,82), Segment(36,38), Segment(10,12), Segment(1,1), Segment(23,23),
#      Segment(32,33), Segment(87,88), Segment(55,56), Segment(69,71), Segment(89,91), Segment(93,93), Segment(38,40),
#      Segment(33,34), Segment(14,16), Segment(57,59), Segment(70,72), Segment(36,36), Segment(29,29), Segment(73,74),
#      Segment(66,68), Segment(36,38), Segment(1,3), Segment(49,50), Segment(68,70), Segment(26,28), Segment(30,30),
#      Segment(1,2), Segment(64,65), Segment(57,58), Segment(58,58), Segment(51,53), Segment(41,41), Segment(17,18),
#      Segment(45,46), Segment(4,4), Segment(0,1), Segment(65,67), Segment(92,93), Segment(84,85), Segment(75,77),
#      Segment(39,41), Segment(15,15), Segment(29,31), Segment(83,84), Segment(12,14), Segment(91,93), Segment(83,84),
#      Segment(81,81), Segment(3,4), Segment(66,67), Segment(8,8), Segment(17,19), Segment(86,87), Segment(44,44),
#      Segment(34,34), Segment(74,74), Segment(94,95), Segment(79,81), Segment(29,29), Segment(60,61), Segment(58,59),
#      Segment(62,62), Segment(54,56), Segment(58,58), Segment(79,79), Segment(89,91), Segment(40,42), Segment(2,4),
#      Segment(12,14), Segment(5,5), Segment(28,28), Segment(35,36), Segment(7,8), Segment(82,84), Segment(49,51),
#      Segment(2,4), Segment(57,59), Segment(25,27), Segment(52,53), Segment(48,49), Segment(9,9), Segment(10,10), Segment(78,78),
#      Segment(26,26), Segment(83,84), Segment(22,24), Segment(86,87), Segment(52,54), Segment(49,51), Segment(63,64), Segment(54,54)],43)
#
# ]:
#     print((compute_optimal_points(segments)), answer)
