import bisect
import math

from_to_maps = dict()
res = math.inf

with open('input.txt', 'r', encoding = 'utf-8') as f:
    k = None
    values = [int(v) for v in f.readline().strip().replace('seeds: ', '').split(' ')]
    seeds = []
    for i in range(0, len(values), 2):
        seeds.append((values[i], values[i]+values[i+1]-1))
    seeds.sort()
    for line in f:
        line = line.strip()
        if line:
            if line.endswith(' map:'):
                k = line.replace(' map:', '').split('-')[-1]
                from_to_maps[k] = list()
            else:
                dst, src, l = line.strip().split(' ')
                bisect.insort_left(from_to_maps[k], (int(src)+int(l), int(src), -int(src)+int(dst)))
    for k, v in from_to_maps.items():
        new_seeds = []
        for l, r in seeds:
            i = bisect.bisect_right(v, l, key = lambda x: x[0])
            # has intersection
            if i != len(v) and v[i][1] <= l < v[i][0]:
                for j in range(i, len(v)):
                    if v[j][1] > r:
                        break
                    f = v[j][2]
                    if l < v[j][1]:
                        new_seeds.append((l, v[j][1]-1))
                        l = v[j][1]
                    new_l = l+f
                    new_r = min(r, v[j][0]-1)+f
                    new_seeds.append((new_l, new_r))
                    if r < v[j][0]:
                        l = r
                        break
                    l += new_r-new_l
                if l < r:
                    new_seeds.append((l, r))
            # no intersection
            else:
                new_seeds.append((l, r))
        seeds = new_seeds
        seeds.sort()
    res = seeds[0][0]
print(res)