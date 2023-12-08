from regex import *
from collections import *
from heapq import *
from time import time, sleep



# input
file = open('sample07.txt')
file = open('input07.txt')
data = file.readlines()

# Point maps
hp = {
    5: int(7e12), # Five of a kind
    4: int(6e12), # Four of a kind
    32: int(5e12), # Full house
    31: int(4e12), # Three of a kind
    22: int(3e12), # Two pair
    12: int(2e12), # One pair
    1: int(1e12)  # High card
    }

np = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
    }

# Point function

def points(hand):
    c = Counter(hand)
    n = len(c)
    
    if n==5:
        sam = hp[1]
    elif n==4:
        sam = hp[12]
    elif n==3:
        v = set(c.values())
        if v == {1,3}:
            sam = hp[31]
        else:
            sam = hp[22]
    elif n==2:
        v = set(c.values())
        if v == {3,2}:
            sam = hp[32]
        else:
            sam = hp[4]
    else:
        sam = hp[5]
    
    for i, c in enumerate(hand):
        sam += np[c] * 10 ** (2*(4-i))
    
    return sam

# Rank function
def rank(hands):
    hi = sorted([[x,i] for i, x in enumerate(hands)], key = lambda x: points(x[0]))
    ranks = [0] * len(hi)
    for i, e in enumerate(hi):
        ranks[e[1]] = i+1
    return ranks

# code starts here
hands = []
bids = []
for line in data:
    hand, bid = line.strip().split()
    bid = int(bid)
    hands.append(hand)
    bids.append(bid)

ranks = rank(hands)

ans = 0
for i in range(len(hands)):
    ans += ranks[i] * bids[i]

print(ans)

    
