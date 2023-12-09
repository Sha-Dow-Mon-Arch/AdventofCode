from regex import *
from collections import *
from heapq import *
from time import time, sleep

# lr map
pick = {
    'L': 0,
    'R': 1
    }

# input
file = open('input08.txt')
data = file.readlines()

lr_seq = data[0].strip()

data = data[2:]
maps = {}

for line in data:
    p, c = line.split('=')
    c = c.strip()[1:-1].split(',')
    maps[p.strip()] = [c[0].strip(), c[1].strip()]

MOD = len(lr_seq)
i = 0
start = 'AAA'
while True:
    if start == 'ZZZ':
        print(i)
        break
    start = maps[start][pick[lr_seq[i%MOD]]]
    i += 1