moves =[(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start, smap, iter=64):
    queue = set([start])
    m, n = len(smap), len(smap[0])
    for _ in range(iter):
        new_queue = set()
        for x, y in queue:
            for a, b in moves:
                xa, yb = x+a, y+b
                if -1<xa<m and -1<yb<n and smap[xa][yb] != '#':
                    new_queue.add((xa, yb))
        queue = new_queue
    return len(queue)

with open('input.txt', 'r', encoding = 'utf-8') as f:
    smap = []
    i = 0
    start = None
    for line in f:
        row = []
        for j, c in enumerate(line):
            row.append(c)
            if c == 'S':
                start = (i, j)
        smap.append(row)
        i += 1
    print(bfs(start, smap))
