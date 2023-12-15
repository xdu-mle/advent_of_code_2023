res = 0

def my_hash(s: str):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()
        for token in line.split(','):
            res += my_hash(token)

print(res)
