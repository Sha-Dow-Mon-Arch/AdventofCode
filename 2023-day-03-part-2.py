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
    #print('chosen:', val)
    return 0

part_nums = []
for num in nums:
    if check(num):
        part_nums.append(num)

stars = {}
for i in range(N):
    for j in range(N):
        if mat[i][j] == '*':
            stars[(i, j)] = []

def check2(param):
    row, s, e, val = param
    if row:
        for j in range(max(0, s-1), min(N, e+2)):
            if mat[row-1][j] == '*':
                stars[(row-1, j)].append(val)
    if row != N-1:
        for j in range(max(0, s-1), min(N, e+2)):
            if mat[row+1][j] == '*':
                stars[(row+1, j)].append(val)
    if s:
        if mat[row][s-1] == '*':
            stars[(row, s-1)].append(val)
    if e != N-1:
        if mat[row][e+1] == '*':
            stars[(row, e+1)].append(val)

for num in part_nums:
    check2(num)
sam = 0
for gear in stars:
    v = stars[gear]
    if len(v) == 2:
        sam += v[0] * v[1]
print(sam)
