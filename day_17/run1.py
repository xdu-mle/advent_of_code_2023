import math
import heapq

moves = {
    'r': (0, 1), # right
    'l': (0, -1), # left
    'd': (1, 0), # down
    'u': (-1, 0) # up
}

turns = {
    'r': {'l': 'u', 'r': 'd'}, # right->left = up, right->right = down
    'l': {'l': 'd', 'r': 'u'}, # left->left = down, left->right = up
    'd': {'l': 'r', 'r': 'l'}, # down->left = right, down->right = left
    'u': {'l': 'l', 'r': 'r'}, # up->left = left, up->right = right
}

def visit(start, end, d, bmap, cnt1=3, cnt2=4):
    cost = math.inf
    visited = set([(start[0], start[1], d, cnt1)])
    m, n = len(bmap), len(bmap[0])
    queue = [(0, start[0], start[1], d, cnt1)]
    while queue:
        cost_c, x_c, y_c, d_c, cnt_c = heapq.heappop(queue)
        nexts = []
        if cnt_c < cnt2:
            nexts.extend(list(turns[d_c].values()))
        if cnt_c > 0:
            nexts.append(d_c)
        for d_n in nexts:
            a, b = moves[d_n]
            x_n, y_n = x_c+a, y_c+b
            cnt_n = cnt1 if d_n != d_c else (cnt_c-1)
            if -1<x_n<m and -1<y_n<n and (x_n, y_n, d_n, cnt_n) not in visited and cnt_n > 0:
                if (x_n, y_n) == end:
                    if cnt_n < cnt2:
                        cost = min(cost_c + bmap[x_n][y_n], cost)
                    else:
                        visited.add((x_n, y_n, d_n, cnt_n))
                else:
                    if bmap[x_n][y_n]+cost_c < cost:
                        visited.add((x_n, y_n, d_n, cnt_n))
                        heapq.heappush(queue, (bmap[x_n][y_n]+cost_c, x_n, y_n, d_n, cnt_n))
    return cost

with open('input.txt', 'r', encoding = 'utf-8') as f:
    bmap = []
    for line in f:
        bmap.append([int(v) for v in list(line.strip())])
    m, n = len(bmap), len(bmap[0])
    print(min(visit((0, 0), (m-1, n-1), 'r', bmap), visit((0, 0), (m-1, n-1), 'd', bmap)))
