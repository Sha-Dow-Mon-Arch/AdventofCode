from regex import *
from collections import *
from heapq import *
from time import time, sleep




# input

t = 49979494
d = 263153213781851
ways = 0
for i in range(1, t+1):
    if i*(t-i) > d:
        ways += 1
print(ways)