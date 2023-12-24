from skspatial.objects import Line
import numpy as np
from numpy import linalg

def get_matrix(vec):
    A = np.zeros((3, 3), dtype = np.float64)
    A[0, 1] = -vec[2]
    A[0, 2] = vec[1]
    A[1, 0] = vec[2]
    A[1, 2] = -vec[0]
    A[2, 0] = -vec[1]
    A[2, 1] = vec[0]
    return A

def get_vector(line):
    return np.cross(line.point, line.direction)

with open('input.txt', 'r', encoding = 'utf-8') as f:
    lines = []
    for line in f:
        part1, part2 = line.strip().split(' @ ')
        x, y, z = map(int, part1.split(', '))
        xv, yv, zv = map(int, part2.split(', '))
        lines.append(Line(point=(x, y, z), direction=(xv, yv, zv)))
    V = np.zeros(6, dtype = np.float64).ravel()
    V[0:3] = -get_vector(lines[0])+get_vector(lines[1])
    V[3:6] = -get_vector(lines[0])+get_vector(lines[2])
    M = np.zeros((6, 6), dtype = np.float64)
    M[0:3, 0:3] = get_matrix(lines[0].direction)-get_matrix(lines[1].direction)
    M[3:6, 0:3] = get_matrix(lines[0].direction)-get_matrix(lines[2].direction)
    M[0:3, 3:6] = -get_matrix(lines[0].point)+get_matrix(lines[1].point)
    M[3:6, 3:6] = -get_matrix(lines[0].point)+get_matrix(lines[2].point)
    res = linalg.solve(M, V)
    print(sum([int(np.round(res[i])) for i in range(3)]))

