import math
import bisect
import time
from collections import defaultdict

st = time.time()
res = 0

maps = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

with open('input.txt', 'r', encoding = 'utf-8') as f:
    min_x, max_x, min_y, max_y = math.inf, 0, math.inf, 0
    levels = defaultdict(list)
    segments = defaultdict(set)
    x, y = 0, 0
    for line in f:
        token = line.strip().split(' ')[-1].replace('#', '').replace('(', '').replace(')', '')
        d = maps[token[-1]]
        cnt = int(token[0:5], base=16)
        # you can use question 1 to test
        # d, cnt, _ = line.strip().split(' ')
        # cnt = int(cnt)
        if d in ('D', 'U'):
            while cnt:
                bisect.insort_left(levels[x], (y, d), key = lambda e: e[0])
                x += 1 if d == 'D' else -1
                cnt -= 1
            bisect.insort_left(levels[x], (y, d), key = lambda e: e[0])
        else:
            py = y
            y += cnt if d == 'R' else -cnt
            segments[x].add(tuple(sorted((py, y))))
    d = levels[0][0][-1]
    for x in sorted(levels.keys()):
        l = 0
        is_inside = False
        py, pd = None, d
        cont = 0
        for y, yd in levels[x]:
            if yd != pd:
                is_inside = not is_inside
            if is_inside or (py is not None and (py, y) in segments[x]):
                l += (y-py) if cont else y-py+1
                cont = 1
            else:
                cont = 0
            py, pd = y, yd
        res += l
print(f'result {res}, using {int(time.time()-st)} seconds')
