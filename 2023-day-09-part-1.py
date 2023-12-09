from regex import *
from collections import *
from heapq import *
from time import time, sleep
from math import ceil, floor, log2, log10, log, gcd
from functools import reduce, cache


# input
file = open('input09.txt')
data = file.readlines()

sam = 0
for line in data:
    nums = list(map(int, line.strip().split()))
    
    n = len(nums)
    mat = [0]*(n+1)
    mat = [mat.copy() for _ in range(n+1)]
    
    mat[0] = nums.copy() + [0]
    
    row = 0
    
    while any(mat[row]):
        row += 1
        for i in range(n - row):
            mat[row][i] = mat[row-1][i+1] - mat[row-1][i]
    #print(row)
    
    #print(*mat, sep = '\n')
    x = row - 1
    y = n - row + 1
    
    #print((x, y))
    
    for i in range(x+1):
        mat[x-i][y+i] = mat[x-i][y+i-1] + mat[x-i+1][y+i-1]
    
    #print("New Matrix")
    
    #print(*mat, sep = '\n')
    sam += mat[0][-1]
print(sam)  

'''
1581679977
'''
    