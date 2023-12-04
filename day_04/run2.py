card_counts = []
with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        card_s, number_s = line.strip().split(': ')[1].split(' | ')
        cards = set([int(v) for v in card_s.split(' ') if v])
        numbers = set([int(v) for v in number_s.split(' ') if v])
        cnt = 0
        for card in cards:
            if card in numbers:
                cnt += 1
        card_counts.append(cnt)
l = len(card_counts)
dp = [1] * l
for i in range(l-1, -1, -1):
    if card_counts[i]:
        for j in range(i+1, min(i+1+card_counts[i], l)):
            dp[i] += dp[j]
print(sum(dp))