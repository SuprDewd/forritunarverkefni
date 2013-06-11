tests = [
    [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ],
    [
        [7, 12, 1, 14],
        [2, 13, 8, 11],
        [16, 3, 10, 5],
        [9, 6, 15, 4]
    ],
    [
        [23, 28, 21],
        [22, 24, 26],
        [27, 20, 25]
    ],
    [
        [37, 78, 29, 70, 21, 62, 13, 54, 5],
        [6, 38, 79, 30, 71, 22, 63, 14, 46],
        [47, 7, 39, 80, 31, 72, 23, 55, 15],
        [16, 48, 8, 40, 81, 32, 64, 24, 56],
        [57, 17, 49, 9, 41, 73, 33, 65, 25],
        [26, 58, 18, 50, 1, 42, 74, 34, 66],
        [67, 27, 59, 10, 51, 2, 43, 75, 35],
        [36, 68, 19, 60, 11, 52, 3, 44, 76],
        [77, 28, 69, 20, 61, 12, 53, 4, 45]
    ],
    [
        [1, 2],
        [3, 4]
    ],
    [
        [1, 2, 3],
        [4, 5, 6],
        [3, 2, 1]
    ],
    [
        [5, 2, 5],
        [2, 5, 2],
        [5, 2, 5]
    ],
    [
        [1, 1, 1],
        [1, 5, 1],
        [1, 1, 1]
    ]
]

def sumr(t, x, y, dx, dy):
    n = len(t)
    s = 0
    while 0 <= x < n and 0 <= y < n:
        s += t[x][y]
        x += dx
        y += dy
    return s

for i, t in enumerate(tests):
    n = len(t)
    for j in range(n):
        assert len(t[j]) == n
    with open('T%d.in' % i, 'w') as f:
        f.write('%d\n' % n)
        for j in range(n):
            f.write(' '.join(map(str, t[j])) + '\n')
    ok = True
    s = sumr(t, 0, 0, 0, 1)
    for j in range(n):
        ok = ok and s == sumr(t, j, 0, 0, 1)
        ok = ok and s == sumr(t, 0, j, 1, 0)

    ok = ok and s == sumr(t, 0, 0, 1, 1)
    ok = ok and s == sumr(t, n-1, 0, -1, 1)

    with open('T%d.out' % i, 'w') as f:
        if ok:
            f.write('galdraferningur\n')
        else:
            f.write('ekki galdraferningur\n')

