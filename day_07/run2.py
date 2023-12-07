from collections import Counter

res = 0

vmap = {
    'J': 1,
    'T': 10,
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

def count_hand(s):
    cnt = Counter()
    for c in s:
        if c.isdigit():
            cnt[int(c)] += 1
        else:
            cnt[vmap[c]] += 1
    if 1 in cnt:
        if cnt[1] != 5:
            max_ks = sorted(cnt.keys(), key = lambda x: cnt[x], reverse = True)[0:2]
            max_k = max_ks[0] if max_ks[0] != 1 else max_ks[-1]
            cnt[max_k] += cnt[1]
            del cnt[1]
    return tuple(sorted(cnt.values(), reverse=True))
        
with open('input.txt', 'r', encoding = 'utf-8') as f:
    card_bets = []
    for line in f:
        card, bet = line.strip().split(' ')
        card_bets.append((card, int(bet)))
    card_bets.sort(key = lambda x:(count_hand(x[0]), convert_to_v_tuple(x[0])))
    for i in range(len(card_bets)):
        print(i+1, card_bets[i], count_hand(card_bets[i][0]), convert_to_v_tuple(card_bets[i][0]))
        res += (i+1)*card_bets[i][-1]
print(res)