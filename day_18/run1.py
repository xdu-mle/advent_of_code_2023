import math
import bisect
from collections import defaultdict

res = 0

with open('input.txt', 'r', encoding = 'utf-8') as f:
    min_x, max_x, min_y, max_y = math.inf, 0, math.inf, 0
    ups = dict()
    edges = set()
    x, y = 0, 0
    for line in f:
        d, cnt, _ = line.strip().split(' ')
        cnt = int(cnt)
        if d in ('D', 'U'):
            while cnt:
                ups[(x, y)] = d
                edges.add((x, y))
                x += 1 if d == 'D' else -1
                cnt -= 1
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                ups[(x, y)] = d
        else:
             while cnt:
                edges.add((x, y))
                y += 1 if d == 'R' else -1
                cnt -= 1
                min_y = min(min_y, y)
                max_y = max(max_y, y)
    for i in range(min_x, max_x+1):
        d = None
        is_inside = False
        l = 0
        for j in range(min_y, max_y+1):
            if (i, j) in edges:
                if d is None or ((i, j) in ups and ups[(i, j)] != d):
                    d = ups[(i, j)]
                    is_inside = not is_inside
                l += 1
            else:
                if is_inside:
                    l += 1
        print(i, l)
        res += l
print(res)
