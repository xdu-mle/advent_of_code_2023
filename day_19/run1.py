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
                    pipelines[pid].append([s[0], s[1:2], int(s[2:]), target])
                else:
                    pipelines[pid].append(rule)
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
                target = None
                for rule in rules:
                    if isinstance(rule, str):
                        target = rule
                        break
                    else:
                        x = rule[0]
                        v = conditions[x]
                        if rule[1] == '<' and v < rule[2]:
                            target = rule[-1]
                            break
                        elif rule[1] == '>' and v > rule[2]:
                            target = rule[-1]
                            break
                pid = target
                if pid in ('A', 'R'):
                    break
            if pid == 'A':
                res += sum(conditions.values())
print(res)
