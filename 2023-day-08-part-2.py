from regex import *
from collections import *
from heapq import *
from time import time, sleep
from math import ceil, floor, log2, log10, log, gcd
from functools import reduce, cache

# lr map
pick = {
    'L': 0,
    'R': 1
    }

# lcm function
def lcm(a, b):
    return (a * b) // gcd(a, b)

# check function
def check(queue):
    for node in queue:
        if node[-1] != 'Z':
            return False
    return True

# input
file = open('input08.txt')
data = file.readlines()

# code starts here
lr_seq = data[0].strip()

data = data[2:]
maps = {}

for line in data:
    p, c = line.split('=')
    c = c.strip()[1:-1].split(',')
    maps[p.strip()] = [c[0].strip(), c[1].strip()]

MOD = len(lr_seq)

queue = deque()
counts = []
for node in maps:
    if node[-1] == 'A':
        i = 0
        while node[-1]!='Z':
            node = maps[node][pick[lr_seq[i%MOD]]]
            i += 1
        counts.append(i)
print(*counts, sep = '\n')
print(reduce(lcm, counts))

