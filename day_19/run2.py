import copy
import math

res = 0

pipelines = dict()

parts = {
    'x': (0, 4001),
    'm': (0, 4001),
    'a': (0, 4001),
    's': (0, 4001)
}

def calculate(parts):
    res = 1
    for a, b in parts.values():
        res *= b-a-1
    return res

def dfs(pid, parts):
    cnt = 0
    new_parts = copy.deepcopy(parts)
    for rule in pipelines[pid]:
        if isinstance(rule, str):
            if rule not in ('A', 'R'):
                cnt += dfs(rule, new_parts)
            elif rule == 'A':
                cnt += calculate(new_parts)
        else:
            x = rule[0]
            v = rule[2]
            part = new_parts[x]
            if part[0] < rule[2] < part[1]:
                if rule[1] == '<':
                    new_parts[x] = (part[0], v)
                    if rule[-1] not in ('A', 'R'):
                        cnt += dfs(rule[-1], new_parts)
                    else:
                        if rule[-1] == 'A':
                            cnt += calculate(new_parts)
                    new_parts[x] = (v-1, part[1])
                else:
                    new_parts[x] = (v, part[1])
                    if rule[-1] not in ('A', 'R'):
                        cnt += dfs(rule[-1], new_parts)
                    else:
                        if rule[-1] == 'A':
                            cnt += calculate(new_parts)
                    new_parts[x] = (part[0], v+1)
    return cnt

with open('input.txt', 'r', encoding = 'utf-8') as f:
    # part 1 pipeline extractions
    for line in f:
        line = line.strip()
        if line:
            pid, rules = line.replace('}', '').split('{')
            pipelines[pid] = list()
            for rule in rules.split(','):
                if ':' in rule:
                    s, target = rule.split(':')
                    # (part, operator, number, target)
                    pipelines[pid].append([s[0], s[1:2], int(s[2:]), target])
                else:
                    pipelines[pid].append(rule)
        else:
            break

print(dfs('in', parts))
