nmap = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
res = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a, b = None, None
        line = line.strip()
        l = len(line)
        i = 0
        while i < l:
            if line[i].isdigit():
                c = line[i]
                if a is None:
                    a = c
                b = c
            else:
                for k in (3, 4, 5):
                    v = line[i:min(i+k, l)]
                    if v in nmap:
                        c = nmap[v]
                        if a is None:
                            a = c
                        b = c
                        break
            i += 1
        res += int(a+b)
print(res)
