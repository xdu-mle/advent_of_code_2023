test_range = (7, 27)
input_range = (200000000000000, 400000000000000)

def line_intersection(x1, y1 ,x2, y2, x3, y3, x4, y4):
    if (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) != 0:
        px = ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
        py = ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        return px, py
    else:
        return None, None

with open('input.txt', 'r', encoding = 'utf-8') as f:
    segments = []
    for line in f:
        part1, part2 = line.strip().split(' @ ')
        x, y, z = map(int, part1.split(', '))
        xv, yv, zv = map(int, part2.split(', '))
        segments.append((x, y, xv, yv))
    n = len(segments)
    cnt = 0
    use_range = input_range
    for i in range(n):
        for j in range(i+1, n):
            x, y = line_intersection(
                segments[i][0],
                segments[i][1],
                segments[i][0]+segments[i][2],
                segments[i][1]+segments[i][3],
                segments[j][0],
                segments[j][1],
                segments[j][0]+segments[j][2],
                segments[j][1]+segments[j][3]
            )
            print(x, y)
            if x and \
                use_range[0] <= x <= use_range[1] and \
                use_range[0] <= y <= use_range[1] and \
                (x-segments[i][0]) / segments[i][2] > 0 and \
                (x-segments[j][0]) / segments[j][2] > 0:
                cnt += 1
    print(cnt)

