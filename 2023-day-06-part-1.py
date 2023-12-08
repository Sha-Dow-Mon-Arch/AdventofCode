from regex import *
from collections import *
from heapq import *
from time import time, sleep




# input

time = list(map(int, input().split(':')[1].strip().split()))
dist = list(map(int, input().split(':')[1].strip().split()))

n = len(time)

ans = 1
for i in range(n):
    t = time[i]
    d = dist[i]
    ways = 0
    for i in range(1, t+1):
        if i*(t-i) > d:
            ways += 1
    ans *= ways
    #print(ways)
print(ans)
        