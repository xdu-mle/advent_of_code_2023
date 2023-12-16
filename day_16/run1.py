moves = [
    # right, index 0
    (0, 1),
    # left, index 1
    (0, -1),
    # down, index 2
    (1, 0),
    # up, index 3
    (-1, 0)
]

def visit(start, bmap):
    m, n = len(bmap), len(bmap[0])
    points = set()
    visited = set()
    queue = set([start])
    while queue:
        new_queue = set()
        for x, y, d in queue:
            points.add((x, y))
            visited.add((x, y, d))
            a, b = moves[d]
            xa, yb = x+a, y+b
            if -1 < xa < m and -1 < yb < n:
                if bmap[xa][yb] == '|' and d in (0, 1):
                    for d in (2, 3):
                        if (xa, yb, d) not in visited:
                            new_queue.add((xa, yb, d)) 
                elif bmap[xa][yb] == '-' and d in (2, 3):
                    for d in (0, 1):
                        if (xa, yb, d) not in visited:
                            new_queue.add((xa, yb, d))
                elif bmap[xa][yb] == '\\':
                    if d == 0:
                        d = 2
                    elif d == 1:
                        d = 3
                    elif d == 2:
                        d = 0
                    else:
                        d = 1
                    if (xa, yb, d) not in visited:
                        new_queue.add((xa, yb, d))
                elif bmap[xa][yb] == '/':
                    if d == 0:
                        d = 3
                    elif d == 1:
                        d = 2
                    elif d == 2:
                        d = 1
                    else:
                        d = 0
                    if (xa, yb, d) not in visited:
                        new_queue.add((xa, yb, d))
                else:
                    if (xa, yb, d) not in visited:
                        new_queue.add((xa, yb, d))
            queue = new_queue
    return len(points)-1
res = 0
with open('input.txt', 'r', encoding = 'utf-8') as f:
    bmap = []
    for line in f:
        bmap.append(list(line.strip()))
# (x, y, direction)
print(visit((0, -1, 0), bmap))
