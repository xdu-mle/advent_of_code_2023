arr = []
res = 0
with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()
        arr.append(list(line))
m, n = len(arr), len(arr[0])
for i in range(m):
    v = 0
    is_near = False
    for j in range(n):
        if arr[i][j].isdigit():
            v = v*10+int(arr[i][j])
            if not is_near:
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if -1<i+a<m and -1<j+b<n:
                            if not arr[i+a][j+b].isdigit() and arr[i+a][j+b] != '.':
                                is_near = True
        else:
            if is_near:
                res += v
            v = 0
            is_near = False
    if is_near:
        res += v
print(res)