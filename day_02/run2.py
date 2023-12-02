from collections import Counter

res = 0
with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        val = Counter()
        line = line.strip()
        games = line.split(': ')[1].split('; ')
        for game in games:
            for play in game.split(', '):
                n, c = play.split(' ')
                val[c] = max(val[c], int(n))
        v = 1
        for cv in val.values():
            v *= cv
        res += v

print(res)