
res = 1

with open('input.txt', 'r', encoding = 'utf-8') as f:
    times = []
    v = 0
    for c in f.readline().replace('Time:', '').strip():
        if c.isdigit():
            v = v*10+int(c)
        else:
            if v:
                times.append(v)
            v = 0
    times.append(v)
    distances = []
    v = 0
    for c in f.readline().replace('Distance:', '').strip():
        if c.isdigit():
            v = v*10+int(c)
        else:
            if v:
                distances.append(v)
            v = 0
    distances.append(v)
    for i in range(len(times)):
        cnt = 0
        for j in range(1, times[i]):
            if j*(times[i]-j) > distances[i]:
                cnt += 1
        res *= cnt
print(res)