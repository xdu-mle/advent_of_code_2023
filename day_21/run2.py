# This solution is applicable to input that grow frontiers in a repeatable pattern
# if the pattern is not repeatable, the solution will be time consuming as brute force method
# please try input_bad.txt to see a bad case
moves =[(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start, smap, iter=26501365):
    m, n = len(smap), len(smap[0])
    queue = set([start])
    visited = set([start])
    n_frontiers = [0] * m
    diff = [0] * m # diff of current n_frontier and n_frontier m steps before
    diff_diff = [0] * m # checking diff cycles, when all diff_diffs are 0
    cnt = [0] * 3
    step = 0
    while step < iter:
        new_queue = set()
        for x, y in queue:
            visited.add((x, y))
            for a, b in moves:
                xa, yb = x+a, y+b
                if smap[xa%m][yb%n] != '#':
                    if (xa, yb) not in visited:
                        visited.add((xa, yb))
                        new_queue.add((xa, yb))
        queue = new_queue
        cnt[2], cnt[0] = cnt[0]+len(queue), cnt[1]
        cnt[1] = cnt[2]
        
        n_frontier = len(queue)
        sm = step % m
        # visit starts to enter corner map through diagonals
        if step >= m:
            # compare number of visits on frontier to m steps before
            # e.g.
            #    □
            #   □□□          □
            #  □□□□□  v.s.  □□□  v.s. □ 
            #   □□□          □
            #    □
            diff_to_last_sm = n_frontier - n_frontiers[sm]
            diff_diff[sm] = diff_to_last_sm - diff[sm]
            diff[sm] = diff_to_last_sm
        n_frontiers[sm] = n_frontier
        step += 1
        if step >= 2*m:
            if all([v==0 for v in diff_diff]):
                break
    for j in range(step, iter):
        jm = j%m
        n_frontiers[jm] += diff[jm]
        cnt[2], cnt[0] = cnt[0]+n_frontiers[jm], cnt[1]
        cnt[1] = cnt[2]
    return cnt[-1]

with open('input.txt', 'r', encoding = 'utf-8') as f:
    smap = []
    i = 0
    start = None
    for line in f:
        row = []
        for j, c in enumerate(line.strip()):
            row.append(c)
            if c == 'S':
                start = (i, j)
        smap.append(row)
        i += 1
    print(bfs(start, smap))
