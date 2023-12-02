cnt = {'red': 12, 'green': 13, 'blue':14}
res = 0
gid = 1
with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()
        games = line.split(': ')[1].split('; ')
        is_add = True
        for game in games:
            for play in game.split(', '):
                n, c = play.split(' ')
                if int(n) > cnt[c]:
                    is_add = False
        if is_add:
            res += gid
        gid += 1
print(res)