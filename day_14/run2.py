from collections import defaultdict, Counter

res = 0

def evaluate(arr):
    res = 0
    m, n = len(arr), len(arr[0])
    for row in range(m):
        for col in range(n):
            if arr[row][col] == 'O':
                res += (m-row)
    return res

def get_val(arr, i, j, vertical=True):
    if vertical:
        return arr[i][j]
    else:
        return arr[j][i]

def move(arr, s1, e1, i1, s2, e2, i2, vertical=True):
    col = s1 + i1
    while min(s1, e1) < col < max(s1, e1):
        i = s2 + i2
        while min(s2, e2) < i < max(s2, e2):
            if get_val(arr, i, col, vertical) not in ('O', '#'):
                j = i+i2
                while min(s2, e2) < j < max(s2, e2) and get_val(arr, j, col, vertical) == '.':
                    j += i2
                if j == e2:
                    break
                if get_val(arr, j, col, vertical) == '#':
                    i = j
                else:
                    if vertical:
                        arr[i][col], arr[j][col] = arr[j][col], arr[i][col]
                    else:
                        arr[col][i], arr[col][j] = arr[col][j], arr[col][i]
            i += i2
        col += i1

arr = []
cycles = Counter()
cycle = None
with open('input.txt', 'r', encoding = 'utf-8') as f:
    hist = []
    hist_map = defaultdict(list)
    for line in f:
        line = line.strip()
        arr.append(list(line))
    m, n = len(arr), len(arr[0])
    iter = None
    for i in range(1000_000_000):
        # to north
        move(arr, -1, n, 1, -1, m, 1, True)
        # to west
        move(arr, -1, m, 1, -1, n, 1, False)
        # to south
        move(arr, -1, n, 1, m, -1, -1, True)
        # to east
        move(arr, -1, m, 1, n, -1, -1, False)
        v = evaluate(arr)
        hist.append(v)
        if v in hist_map and i-hist_map[v][-1] > 1:
            cycles[i-hist_map[v][-1]] += 1
            if cycles[i-hist_map[v][-1]] == i-hist_map[v][-1]:
                cycle = i-hist_map[v][-1]
                break
        hist_map[v].append(i)
cycle_list = hist[len(hist)-cycle:len(hist)].copy()
print(cycle_list[(1000_000_000-len(hist)-1)%(cycle)])
