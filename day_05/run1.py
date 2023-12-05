import bisect
import math

from_to_maps = dict()
res = math.inf

with open('input.txt', 'r', encoding = 'utf-8') as f:
    k = None
    seeds = [int(v) for v in f.readline().strip().replace('seeds: ', '').split(' ')]
    for line in f:
        line = line.strip()
        if line:
            if line.endswith(' map:'):
                k = line.replace(' map:', '').split('-')[-1]
                from_to_maps[k] = list()
            else:
                dst, src, l = line.strip().split(' ')
                bisect.insort_left(from_to_maps[k], (int(src)+int(l), int(src), -int(src)+int(dst)))
    for seed in seeds:
        for k, v in from_to_maps.items():
            i = bisect.bisect_right(v, seed, key = lambda x: x[0])
            if i != len(v) and v[i][1] <= seed < v[i][0]:
                seed += v[i][2]
        res = min(res, seed)
print(res)