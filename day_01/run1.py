res = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a, b = None, None
        for c in line.strip():
            if c.isdigit():
                if a is None:
                    a = c
                b = c
        res += int(a+b)
print(res)
