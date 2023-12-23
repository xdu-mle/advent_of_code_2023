from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
from functools import cache

moves = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

m, n = None, None
xe, ye = None, None
area = []
visited = set()

def dfs(xs, ys):
    dist = 0
    if area[xs][ys] == '.':
        nxts = list(moves.values())
    else:
        nxts = [moves[area[xs][ys]]]
    for a, b in nxts:
        xa, yb = xs+a, ys+b
        if -1<xa<m and -1<yb<n and (xa, yb) not in visited and area[xa][yb] != '#':
            if xa == xe and yb == ye:
                return 1
            visited.add((xa, yb))
            dist = max(dist, dfs(xa, yb)+1)
            visited.remove((xa, yb))
    return dist

with open('test.txt', 'r', encoding = 'utf-8') as f:
    area = []
    # extract map
    for line in f:
        line = line.strip()
        area.append(line)
    m, n = len(area), len(area[0])
    xe, ye = len(area)-1, area[-1].index('.')
    print(dfs(0, area[0].index('.')))
