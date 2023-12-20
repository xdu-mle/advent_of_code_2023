from collections import defaultdict
import math

class FlipFlop:
    def __init__(self):
        # 0 is off and 1 is on
        self.__status = 0

    def receive_and_send(self, sender:str, pulse: int):
        if pulse == 0:
            self.__status = 1-self.__status
            # 0 is low and 1 is high
            return self.__status
        else:
            return None

class Conjunction:
    def __init__(self):
        self.__memory = dict()
        self.__cnt = {0: 0, 1:0}
    
    def add_sender(self, sender: str):
        self.__memory[sender] = 0
        self.__cnt[0] += 1
    
    def receive_and_send(self, sender:str, pulse: int):
        prv = self.__memory[sender]
        self.__memory[sender] = pulse
        self.__cnt[prv] -= 1
        self.__cnt[pulse] += 1
        if self.__cnt[1] == len(self.__memory):
            return 0
        else:
            return 1

def push_button(modules, connections):
    mem = dict()
    iter = 1
    while True:
        cnt = 0
        queue = [('broadcaster', 0)]
        while queue:
            cur, pulse = queue.pop(0)
            for nxt in connections[cur]:
                if nxt != 'rx':
                    nxt_pulse = modules[nxt].receive_and_send(cur, pulse)
                    if nxt_pulse is not None:
                        queue.append((nxt, nxt_pulse))
                    if nxt in ('js', 'zb', 'bs', 'rr') and nxt not in mem and nxt_pulse == 1:
                        mem[nxt] = iter
        if len(mem) == 4:
            break
        iter += 1
    return math.lcm(*list(mem.values()))

with open('input.txt', 'r', encoding = 'utf-8') as f:
    modules = dict()
    connections = defaultdict(list)
    # part 1 modules and connections extractions
    for line in f:
        line = line.strip()
        cur, nxts = line.split(' -> ')
        if cur == 'broadcaster':
            cur = '&broadcaster'
        if cur != '&broadcaster':
            modules[cur[1:]] = FlipFlop() if cur[0] == '%' else Conjunction()
        for nxt in nxts.split(', '):
            connections[cur[1:]].append(nxt)
    for cur in connections:
        for nxt in connections[cur]:
            if nxt in modules and isinstance(modules[nxt], Conjunction):
                modules[nxt].add_sender(cur)
reverse_connections = defaultdict(list)
for cur in connections:
    for nxt in connections[cur]:
        reverse_connections[nxt].append(cur)
print('Need to use minimum common multiple to calculate unified cycle of', reverse_connections['hb'])
print(push_button(modules, connections))
