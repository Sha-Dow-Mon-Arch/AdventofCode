sam = 0
for gn in range(1, 101):
    d = {
        'red': 0,
        'blue': 0,
        'green': 0
        }
    w = input().split(':')
    w = w[1]
    w = w.split(';')
    for i in range(len(w)):
        w[i] = w[i].split(',')
        for j in range(len(w[i])):
            w[i][j] = w[i][j].split()
    for turn in w:
        for col in turn:
            d[col[1]] = max(d[col[1]], int(col[0]))
    ans = d['red'] * d['blue'] * d['green']
    sam += ans
print(sam)
