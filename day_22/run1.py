from collections import defaultdict

def intersect(rect1, rect2):
    return rect1[1] <= rect2[3] and rect2[1] <= rect1[3] and rect1[0] <= rect2[2] and rect2[0] <= rect1[2]

#print(intersect((1, 0, 1, 2), (0, 0, 2, 0)))

with open('input.txt', 'r', encoding = 'utf-8') as f:
    cid = 0
    cubics = []
    # extract all cubics
    for line in f:
        line = line.strip()
        points = line.split('~')
        x1, y1, z1 = map(int, points[0].split(','))
        x2, y2, z2 = map(int, points[1].split(','))
        cubics.append((x1, y1, x2, y2, z1, z2+1, cid))
        cid += 1
    # sort cubics according to z1 ascending
    cubics.sort(key = lambda cubic: cubic[4])
    # simulate falling
    supported = [set() for _ in range(len(cubics))]
    levels = defaultdict(list)
    for x1, y1, x2, y2, z1, z2, cid in cubics:
        cl = None
        # from high to low
        for l in sorted(levels.keys(), reverse = True):
            for cubic in levels[l]:
                if intersect((x1, y1, x2, y2), cubic):
                    # update holding information
                    supported[cid].add(cubic[-1])
                    if cl is None:
                        cl = l+z2-z1
            if cl is not None:
                break
        # cl is None means to the ground
        if cl is None:
            cl = z2-z1
        # put the cubic with larger z first
        levels[cl].append((x1, y1, x2, y2, cid))
    not_disintegrated = set()
    for sd in supported:
        if len(sd) == 1:
            not_disintegrated.add(list(sd)[0])
    print(len(cubics)-len(not_disintegrated))
