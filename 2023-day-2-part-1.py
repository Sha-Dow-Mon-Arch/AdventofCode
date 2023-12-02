d = {
    'red' : 12,
    'blue' : 14,
    'green' : 13
    }

sam = 0
for gn in range(1, 101):
    w = input().split(':')
    w = w[1]
    w = w.split(';')
    for i in range(len(w)):
        w[i] = w[i].split(',')
        for j in range(len(w[i])):
            w[i][j] = w[i][j].split()
    flag = 0
    for turn in w:
        for col in turn:
            if d[col[1]] < int(col[0]):
                flag = 1
                break
        if flag:
            break
    else:
        sam += gn
print(sam)