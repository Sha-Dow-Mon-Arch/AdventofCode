from regex import *
from collections import *
from heapq import *
from time import time, sleep




# input

seeds = input().split(':')
seeds = seeds[1].strip().split()
seeds = list(map(int, seeds))
input()

N = len(seeds)

sts = {}

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    for seed in seeds:
        if seed in range(s, s+w):
            sts[seed] = seed - s + d
for seed in seeds:
    if seed not in sts:
        sts[seed] = seed

stf = {}

seeds1 = list(sts.values())

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    for seed in seeds1:
        if seed in range(s, s+w):
            stf[seed] = seed - s + d
for seed in seeds1:
    if seed not in stf:
        stf[seed] = seed

ftw = {}

seeds2 = list(stf.values())

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    for seed in seeds2:
        if seed in range(s, s+w):
            ftw[seed] = seed - s + d
for seed in seeds2:
    if seed not in ftw:
        ftw[seed] = seed

wtl = {}

seeds3 = list(ftw.values())

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    for seed in seeds3:
        if seed in range(s, s+w):
            wtl[seed] = seed - s + d
for seed in seeds3:
    if seed not in wtl:
        wtl[seed] = seed

ltt = {}

seeds4 = list(wtl.values())

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    for seed in seeds4:
        if seed in range(s, s+w):
            ltt[seed] = seed - s + d
for seed in seeds4:
    if seed not in ltt:
        ltt[seed] = seed

tth = {}

seeds5 = list(ltt.values())

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    for seed in seeds5:
        if seed in range(s, s+w):
            tth[seed] = seed - s + d
for seed in seeds5:
    if seed not in tth:
        tth[seed] = seed

htl = {}

seeds6 = list(tth.values())

input()
while True:
    _ = input()
    if _ == '':
        break
    d, s, w = map(int, _.split())
    for seed in seeds6:
        if seed in range(s, s+w):
            htl[seed] = seed - s + d
for seed in seeds6:
    if seed not in htl:
        htl[seed] = seed

#print(sts, stf, ftw, wtl, ltt, tth, htl, sep = '\n')
print(min(htl.values()))