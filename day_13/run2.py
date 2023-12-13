res = 0

def vertical_check(arr, target = 0):
    max_s = 0
    row = -1
    n = len(arr[0])
    l = len(arr)
    for i in range(1, l):
        cnt = 0
        s = min(i, l-i)
        if s < max_s:
            break
        for j in range(1, s+1):
            if arr[i-j] != arr[i+j-1]:
                for k in range(n):
                    if arr[i-j][k] != arr[i+j-1][k]:
                        cnt += 1
        if cnt == target and s > max_s:
            row = i
            max_s = s
    return row

def horizontal_check(arr, target = 0):
    max_s = 0
    col = -1
    n = len(arr)
    l = len(arr[0])
    for i in range(1, l):
        cnt = 0
        s = min(i, l-i)
        if s < max_s:
            break
        for j in range(1, s+1):
            for k in range(n):
                if arr[k][i-j] != arr[k][i+j-1]:
                    cnt += 1
        if cnt == target and s > max_s:
            col = i
            break
    return col

with open('input.txt', 'r', encoding = 'utf-8') as f:
    arr = []
    for line in f:
        line = line.strip()
        if line:
            arr.append(line)
        else:
            rid = vertical_check(arr, 1)
            if rid != -1:
                res += 100 * rid
            else:
                cid = horizontal_check(arr, 1)
                if cid != -1:
                    res += cid
            arr = []
    if arr:
        rid = vertical_check(arr, 1)
        if rid != -1:
            res += 100 * rid
        else:
            cid = horizontal_check(arr, 1)
            if cid != -1:
                res += cid
print(res)
