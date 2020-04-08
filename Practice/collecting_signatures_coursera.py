
from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

print("Running")
x = ([Segment(1, 3), Segment(2, 5), Segment(3, 6)], 1)

n, *data = map(int, .split())
input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
print(input_segments)