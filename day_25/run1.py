import numpy as np

# modified from https://en.wikipedia.org/wiki/Stoer%E2%80%93Wagner_algorithm
# need to wait several minutes > 5 mins
# Karger's algorithm would be faster for this question

class Union:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.w = [1] * n
        self.c = n
    
    def find(self, x):
        while x != self.p[x]:
            x = self.p[x]
        return x
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.w[x] < self.w[y]:
                self.p[x] = y
                self.w[y] += self.w[x]
                self.c -= 1
            else:
                self.p[y] = x
                self.w[x] += self.w[y]
                self.c -= 1

def global_min_cut(graph):
    ii32 = np.iinfo(np.int32)
    best = [ii32.max, 0]
    n = graph.shape[0]
    co = Union(n)
    for i in range(1, n):
        s, t, w = 0, 0, graph[0].copy()
        for j in range(n-i):
            w[t] = ii32.min
            s, t = t, np.argmax(w)
            for k in range(n):
                w[k] += graph[t][k]
        if w[t] - graph[t][t] < best[0]:
            best = [w[t] - graph[t][t], co.w[co.find(t)]]
        co.union(co.find(s), co.find(t))
        for j in range(n):
            graph[s][j] += graph[t][j]
        for j in range(n):
            graph[j][s] = graph[s][j]
        graph[0][t] = ii32.min
    return best


with open('input.txt', 'r', encoding = 'utf-8') as f:
    nodes = dict()
    for line in f:
        node, children = line.strip().split(': ')
        if node not in nodes:
            nodes[node] = len(nodes)
        for child in children.split(' '):
            if child not in nodes:
                 nodes[child] = len(nodes)
    f.seek(0)
    n = len(nodes)
    graph = np.zeros((n, n), dtype = np.int32)
    for line in f:
        node, children = line.strip().split(': ')
        for child in children.split(' '):
            a, b = nodes[node], nodes[child]
            graph[a][b] = 1
            graph[b][a] = 1
    result = global_min_cut(graph)
    print((len(nodes)-result[1])*result[1])
