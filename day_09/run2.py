def calculate_next(arr):
    cnt = 1
    diff = []
    for i in range(1, len(arr)):
        d = arr[i]-arr[i-1]
        if diff and d == diff[-1]:
            cnt += 1
        diff.append(d)
    if cnt == len(diff):
        return arr[0]-diff[0]
    else:
        return arr[0]-calculate_next(diff)

res = 0

with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        arr = [int(v) for v in line.strip().split(' ')]
        res += calculate_next(arr)

print(res)