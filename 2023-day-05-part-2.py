from regex import *
from collections import *
from heapq import *
from time import time, sleep

def fun1(queue, temp):
    res = []
    for s1, d1, w1 in temp:
        l1, r1 = d1, d1 + w1 - 1 
        for s2, d2, w2 in queue:
            l2, r2 = s2, s2 + w2 - 1
            
            if l2 <= l1 <= r1 <= r2:
                res.append((s1, (l1-l2) + d2, w1))
                break
            if l1 <= l2 <= r2 <= r1:
                res.append((s1 + (l2-l1), d2, w2))
                if l2-l1:
                    temp.append((s1, d1, l2-l1))
                if r1-r2:
                    temp.append((s1 + (l2-l1) + w2-1, d1 + (l2-l1) + w2-1, r1-r2))
                break
            if r1 < l2 or r2 < l1:
                continue
            if l1 <= l2:
                res.append((s1 + (l2-l1), d2, r1 - l2 + 1))
                temp.append((s1, d1, l2-l1))
                break
            if l2 <= l1:
                res.append((s1, d2 + (l1-l2), r2 - l1 + 1))
                temp.append((s1 + (r2-l1)+1, d1 + (r2-l1)+1, r1-r2))
                break
        else:
            res.append((s1, d1, w1))
    return res


# input

seeds = input().split(':')
seeds = seeds[1].strip().split()
seeds = list(map(int, seeds))
n = len(seeds)
temp = []
for i in range(n):
    if i&1:
        continue
    s, w = seeds[i], seeds[i+1]
    temp.append((s, s, w))
seeds = temp
input()

N = len(seeds)

queue = []

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    queue.append((s, d, w))

sts = fun1(queue, temp)
#print(*sts, sep = '\n')

queue = []

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    queue.append((s, d, w))

stf = fun1(queue, sts)
#print(*stf, sep = '\n')

queue = []

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    queue.append((s, d, w))

ftw = fun1(queue, stf)
#print(*ftw, sep = '\n')

queue = []

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    queue.append((s, d, w))

wtl = fun1(queue, ftw)
#print(*wtl, sep = '\n')

queue = []

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    queue.append((s, d, w))

ltt = fun1(queue, wtl)
#print(*ltt, sep = '\n')

queue = []

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    queue.append((s, d, w))

tth = fun1(queue, ltt)
print(*tth, sep = '\n')

queue = []

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    queue.append((s, d, w))

htl = fun1(queue, tth)
#print(*htl, sep = '\n')
print("Answer:", min(htl, key = lambda x: x[1])[1])
