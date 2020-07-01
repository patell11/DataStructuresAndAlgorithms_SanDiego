

def optimal_points(segments):
    segments = sorted(segments, key=lambda x:x[1])

    points = []
    points.append(segments[0][1])
    for i in range(len(segments)):
        if not points[-1] in range(segments[i][0], segments[i][1]+1):
            points.append(segments[i][1])
    return points


if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        a, b = map(int, input().split())
        segments.append((a,b))
    output = optimal_points(segments)
    print(len(output))
    print(*output)