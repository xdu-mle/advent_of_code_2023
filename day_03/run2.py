from collections import defaultdict
arr = []
res = 0
with open('test2.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()
        arr.append(list(line))
m, n = len(arr), len(arr[0])
gears = defaultdict(set)
for i in range(m):
    v = 0
    stars = set()
    for j in range(n):
        if arr[i][j].isdigit():
            v = v*10+int(arr[i][j])
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if -1<i+a<m and -1<j+b<n:
                        if not arr[i+a][j+b].isdigit() and arr[i+a][j+b] == '*':
                            stars.add((i+a, j+b))
        else:
            for star in stars:
                gears[star].add(v)
            stars = set()
            v = 0
    if v != 0:
        for star in stars:
            gears[star].add(v)
for i in gears:
    if len(gears[i]) == 2:
        gl = list(gears[i])
        res += gl[0] * gl[1]
print(res)