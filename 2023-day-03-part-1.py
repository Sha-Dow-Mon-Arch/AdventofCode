mat = []
nums = [] # row, col1, col2, val
N = 140
for i in range(N):
    w = list(input())
    mat.append(w.copy())
    num = ''
    count = 0
    for j, c in enumerate(w):
        if c.isdigit():
            num += c
            count += 1
        elif count != 0:
            nums.append((i, j-count, j-1, int(num)))
            count = 0
            num = ''
            
    if count:
        nums.append((i, j-count+1, j, int(num)))

def check(param):
    row, s, e, val = param
    if row:
        for j in range(max(0, s-1), min(N, e+2)):
            if mat[row-1][j].isdigit():
                continue
            if mat[row-1][j] == '.':
                continue
            return val
    if row != N-1:
        for j in range(max(0, s-1), min(N, e+2)):
            if mat[row+1][j].isdigit():
                continue
            if mat[row+1][j] == '.':
                continue
            return val
    if s:
        if mat[row][s-1].isdigit() or mat[row][s-1] == '.':
            pass
        else:
            return val
    if e != N-1:
        if mat[row][e+1].isdigit() or mat[row][e+1] == '.':
            pass
        else:
            return val
    return 0

sam = 0
for num in nums:
    sam += check(num)
print(sam)
