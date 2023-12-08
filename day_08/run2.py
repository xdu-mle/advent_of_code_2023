from collections import defaultdict, Counter
import bisect
import math

mmap = {'L': 0, 'R':1}

res = 0

def calculate_cycle(start, moves):
    cnt, i, l = 0, 0, len(moves)
    queue = set([start])
    hist = defaultdict(list)
    stop = False
    target = None
    while not stop:
        cnt += 1
        new_queue = set()
        for cur in queue:
            nxt = graph[cur][mmap[moves[i]]]
            new_queue.add(nxt)
            target = (nxt, moves[i])
            if target in hist and hist[target] and (cnt-hist[target][-1]) % l == 0:
                stop = True
                break
            hist[target].append(cnt)
        queue = new_queue
        i = (i+1) % l
    ends = set()
    print(target, hist[target][-1], cnt)
    for k in hist.keys():
        if k[0].endswith('Z'):
            print(hist[k])
            for j in hist[k]:
                if j >= hist[target][-1]:
                    ends.add(j)
    return ends, cnt-hist[target][-1]

with open('input.txt', 'r', encoding = 'utf-8') as f:
    moves = f.readline().strip()
    f.readline()
    graph = dict()
    for line in f:
        cur, nexts = line.strip().split(' = ')
        graph[cur] = nexts.replace('(', '').replace(')', '').split(', ')
    queues = []
    cycles = []
    for node in graph:
        if node.endswith('A'):
            queue, cycle = calculate_cycle(node, moves)
            queues.append(queue)
            cycles.append(cycle)
    print(queues, cycles)
# by problem design, the cycle is around node end with Z
# use Least Common Multiple to calculate all stops at Z 
print(math.lcm(*cycles))
