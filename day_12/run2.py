from functools import cache

res = 0

@cache
def visit(i: int, j: int, cnt: int, s, a):
    if i == len(s) and (j == len(a) or (j == len(a)-1 and cnt == a[j])):
        return 1
    cnt1, cnt2 = 0, 0
    if i < len(s):
        if s[i] in ('?', '#'):
            if j < len(a) and cnt+1 <= a[j]:
                cnt1 = visit(i+1, j, cnt+1, s, a)
        if s[i] in ('?', '.'):
            if cnt == 0:
                cnt2 = visit(i+1, j, 0, s, a)
            else:
                if j < len(a) and a[j] == cnt:
                    cnt2 = visit(i+1, j+1, 0, s, a)
    return cnt1+cnt2

with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()
        s, a = line.split(' ')
        s = '?'.join([s]*5)
        a = [int(v) for v in ','.join([a]*5).split(',')]
        res += visit(0, 0, 0, s, tuple(a))

print(res)
