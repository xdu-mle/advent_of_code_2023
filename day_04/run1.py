res = 0
with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        card_s, number_s = line.strip().split(': ')[1].split(' | ')
        cards = set([int(v) for v in card_s.split(' ') if v])
        numbers = set([int(v) for v in number_s.split(' ') if v])
        cnt = 0
        for card in cards:
            if card in numbers:
                cnt += 1
        if cnt:
            res += 2 ** (cnt-1)
print(res)