from collections import Counter

res = 0

vmap = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

def convert_to_v_tuple(s):
    t = []
    for c in s:
        if c.isdigit():
            t.append(int(c))
        else:
            t.append(vmap[c])
    return tuple(t)

with open('input.txt', 'r', encoding = 'utf-8') as f:
    card_bets = []
    for line in f:
        card, bet = line.strip().split(' ')
        card_bets.append((card, int(bet)))
    card_bets.sort(key = lambda x:(sorted(Counter(x[0]).values(), reverse=True), convert_to_v_tuple(x[0])))
    for i in range(len(card_bets)):
        res += (i+1)*card_bets[i][-1]
print(res)