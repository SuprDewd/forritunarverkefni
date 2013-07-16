from random import randint
ts = 20

for t in range(ts):
    n = randint(3, 5)
    arr = []
    for i in range(n):
        while True:
            x = randint(-100, 100)
            if x not in arr: break

        arr.append(x)

    with open('T%d.in' % t, 'w') as f: f.write('%s\n' % ' '.join(map(str, arr)))
    arr.sort()
    arr[0], arr[1] = arr[1], arr[0]
    with open('T%d.out' % t, 'w') as f: f.write('%s\n' % ' '.join(map(str, arr)))

