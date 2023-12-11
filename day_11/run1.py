res = 0

def dist(a, b, c, d, row_cnt, col_cnt, m, n):
    a, b = min(a, b), max(a, b)
    c, d = min(c, d), max(c, d)
    dist = 0
    for i in range(a+1, b+1):
        dist += 1
        if row_cnt[i] == n:
            dist += 1
    for i in range(c+1, d+1):
        dist += 1
        if col_cnt[i] == m:
            dist += 1
    return dist

with open('input.txt', 'r', encoding = 'utf-8') as f:
    map = list()
    for line in f:
        line = line.strip()
        map.append(list(line))
    m, n = len(map), len(map[0])
    row_cnt, col_cnt = [0] * m, [0] * n
    galaxies = []
    for i in range(m):
        for j in range(n):
            if map[i][j] == '.':
                row_cnt[i] += 1
                col_cnt[j] += 1
            else:
                galaxies.append((i, j))
    l = len(galaxies)
    for i in range(l):
        for j in range(i+1, l):
            res += dist(galaxies[i][0], galaxies[j][0], galaxies[i][1], galaxies[j][1], row_cnt, col_cnt, m, n)

print(res)
