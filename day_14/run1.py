res = 0

def move(arr):
    m, n = len(arr), len(arr[0])
    for col in range(n):
        i = 0
        while i < m:
            if arr[i][col] in ('O', '#'):
                i += 1
                continue
            j = i+1
            while j < m and arr[j][col] == '.':
                j += 1
            if j == m:
                break
            if arr[j][col] == '#':
                i = j
            else:
                arr[i][col], arr[j][col] = arr[j][col], arr[i][col]
                i += 1

with open('input.txt', 'r', encoding = 'utf-8') as f:
    arr = []
    for line in f:
        line = line.strip()
        arr.append(list(line))
    m, n = len(arr), len(arr[0])
    move(arr)
    for row in range(m):
        for col in range(n):
            if arr[row][col] == 'O':
                res += (m-row)
print(res)
