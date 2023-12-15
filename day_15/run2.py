res = 0

def my_hash(s: str):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

hash_map = [dict() for _ in range(256)]

with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()
        for token in line.split(','):
            if '=' in token:
                k, v = token.split('=')
                h = my_hash(k)
                hash_map[h][k] = int(v)
            else:
                k = token.replace('-', '')
                h = my_hash(k)
                if k in hash_map[h]:
                    del hash_map[h][k]
    for i in range(256):
        for j, k in enumerate(hash_map[i].keys()):
            res += (i+1)*(j+1)*hash_map[i][k]
print(res)
