res = 0

moves = {
    '|': {(1, 0), (-1, 0)},
    '-': {(0, 1), (0, -1)},
    'L': {(-1, 0), (0, 1)},
    'J': {(-1, 0), (0, -1)},
    '7': {(1, 0), (0, -1)},
    'F': {(1, 0), (0, 1)},
    'S': {(0, -1), (-1, 0), (1, 0), (0, 1)},
    '.': {}
}

# Set of symbols to indicate inside and outside
insides = {'|', '7', 'F'}

def visit(start, graph):
    cnt = 0
    m, n = len(graph), len(graph[0])
    queue = set([start])
    visited = set()

    while queue:
        new_queue = set()
        for cur in queue:
            visited.add(cur)
            x, y = cur
            for a, b in moves[graph[x][y]]:
                xa, yb = x+a, y+b
                if -1<xa<m and -1<yb<n and (xa, yb) not in visited and (-a, -b) in moves[graph[xa][yb]]:
                    if (x, y) == start and (a, b) == (0, 1):
                        insides.add('S')
                    new_queue.add((xa, yb))
        queue = new_queue

    for i in range(m):
        is_in = False
        for j in range(n):
            if graph[i][j] in insides and (i, j) in visited:
                is_in = not is_in
            else:
                if is_in and (i, j) not in visited:
                    cnt += 1
    return cnt
start = None
with open('input.txt', 'r', encoding = 'utf-8') as f:
    graph = list()
    i = 0
    for line in f:
        line = line.strip()
        graph.append(list(line))
        j = line.find('S')
        if j != -1:
            start = (i, j)
        i += 1
    res = visit(start, graph)
print(res)
