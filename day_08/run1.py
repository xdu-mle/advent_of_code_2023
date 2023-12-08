mmap = {'L': 0, 'R':1}

res = 0

with open('test2.txt', 'r', encoding = 'utf-8') as f:
    moves = f.readline().strip()
    f.readline()
    graph = dict()
    for line in f:
        cur, nexts = line.strip().split(' = ')
        graph[cur] = nexts.replace('(', '').replace(')', '').split(', ')
    queue = set(['AAA'])
    i, l = 0, len(moves)
    while True:
        res += 1
        new_queue = set()
        for cur in queue:
            new_queue.add(graph[cur][mmap[moves[i]]])
        if 'ZZZ' in new_queue:
            break
        queue = new_queue
        i = (i+1)%l

print(res)
