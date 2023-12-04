from regex import *
from collections import *
from heapq import *
from time import time, sleep

N = 223
ans = 0
cards = []
for i in range(1, N+1):
    w = input()
    w = w.split(':')[1]
    w = w.split('|')
    win = w[0].strip().split()
    me = w[1].strip().split()
    
    count = 0
    for num in me:
        if num in win:
            count += 1
    
    cards.append([i, count])
#print(*cards, sep = '\n')

dp = [1] * N

for i in range(N-1, -1, -1):
    num, count = cards[i]
    for j in range(i, i+count):
        dp[i] += dp[j+1]

#print(dp)
print(sum(dp))
    
