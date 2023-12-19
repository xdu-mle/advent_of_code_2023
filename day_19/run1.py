from collections import defaultdict
import math

res = 0

pipelines = dict()

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
                    if s[1:2] == '<':
                        pipelines[pid].append([s[0], -math.inf, int(s[2:]), target])
                    else:
                        pipelines[pid].append([s[0], int(s[2:]), math.inf, target])
                else:
                    pipelines[pid].append([None, rule])
        else:
            break
    # part 2 execute workflows
    for line in f:
        line = line.strip()
        if line:
            conditions = dict()
            for token in line.replace('{', '').replace('}', '').split(','):
                x, v = token.split('=')
                conditions[x] = int(v)
            pid = 'in'
            while True:
                rules = pipelines[pid]
                for rule in rules:
                    if rule[0] is None or rule[1] < conditions[rule[0]] < rule[2]:
                        pid = rule[-1]
                        break
                if pid in ('A', 'R'):
                    break
            if pid == 'A':
                res += sum(conditions.values())
print(res)
