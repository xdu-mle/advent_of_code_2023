import copy
from collections import defaultdict, deque

moves = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

m, n = None, None
xs, ys = None, None
xe, ye = None, None
area = []

def get_neighbours(x, y, area):
    neighbours = []
    for a, b in moves.values():
        xa, yb = x+a, y+b
        if -1<xa<m and -1<yb<n and area[xa][yb] != '#':
            neighbours.append((xa, yb))
    return neighbours

def get_edge(x1, y1, x2, y2,area):
    d = 1
    prv = (x1, y1)
    while x2 != xe or y2 != ye:
        neighbours = get_neighbours(x2, y2, area)
        if len(neighbours) == 2:
            for neighbour in neighbours:
                if neighbour != prv:
                    prv = (x2, y2)
                    x2, y2 = neighbour
                    break
        elif len(neighbours) == 1:
            return None, None, None
        else:
            break
        d += 1
    return x2, y2, d

def get_graph(xs, ys, area):
    graph = defaultdict(dict)
    queue = [(xs, ys)]
    visited = set([(xs, ys)])
    while queue:
        x, y = queue.pop()
        for a, b in moves.values():
            xa, yb = x+a, y+b
            if -1<xa<m and -1<yb<n and (xa, yb) not in visited and area[xa][yb] != '#':
                ex, ey, d = get_edge(x, y, xa, yb, area)
                if d is not None:
                    queue.append((ex, ey))
                    visited.add((xa, yb))
                    visited.add((ex, ey))
                    v = 0
                    if (ex, ey) in graph[(x, y)]:
                        v = graph[(x, y)][(ex, ey)]
                    graph[(x, y)][(ex, ey)] = max(d, v)
                    graph[(ex, ey)][(x, y)] = max(d, v)
    return graph

def dfs(start, end, graph):
    dist = 0
    queue = [(0, start, {start})]
    while queue:
        d, cur, visited = queue.pop()
        for nxt in graph[cur]:
            if nxt == end:
                dist = max(dist, d+graph[cur][nxt])
            else:
                if nxt not in visited:
                    queue.append((d+graph[cur][nxt], nxt, visited | {nxt}))
    return dist

with open('input.txt', 'r', encoding = 'utf-8') as f:
    area = []
    # extract map
    for line in f:
        line = line.strip()
        area.append(line)
    m, n = len(area), len(area[0])
    xs, ys = 0, area[0].index('.')
    xe, ye = len(area)-1, area[-1].index('.')
    graph = get_graph(xs, ys, area)
    # for x, y in sorted(graph.keys()):
    #     print(x, y, graph[(x, y)])
    print(dfs((xs, ys), (xe, ye), graph))
