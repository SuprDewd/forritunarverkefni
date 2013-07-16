from random import randint

ts = 13

def mult(a, b):
    return [ [ sum( p * q for p, q in zip(x, y) ) for y in zip(*b) ] for x in a ]

for t in range(ts):
    n = randint(2, 20)
    k = randint(0, 10)
    a = randint(0, n-1)
    b = randint(0, n-1)
    arr = [ [ randint(0, 1) for j in range(n) ] for i in range(n) ]
    res = [ [ 1 if i == j else 0  for j in range(n) ] for i in range(n) ]

    for x in range(k):
        res = mult(res, arr)

    with open('T%d.in' % t, 'w') as f: f.write('%d\n%s\n%d %d %d\n' % (n, '\n'.join(' '.join(map(str, r)) for r in arr), k, a, b))
    with open('T%d.out' % t, 'w') as f: f.write('%d\n' % res[a][b])

