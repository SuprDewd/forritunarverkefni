from random import randint
ts = 11
for t in range(ts):
    n = randint(1, 100)
    arr = []
    while len(arr) < n:
        a = randint(1, 1000)
        b = randint(1, 1000)
        if not any( a*x[1] == x[0]*b for x in arr ):
            arr.append((a, b))

    with open('T%d.in' % t, 'w') as f: f.write(('%d\n' % n) + ''.join( '%d/%d\n' % x for x in arr ))
    arr.sort(lambda a,b: -1 if a[0] * b[1] < a[1] * b[0] else 1)
    with open('T%d.out' % t, 'w') as f: f.write(''.join( '%d/%d\n' % x for x in arr ))

