tests = [ 1, 2, 5, 10, 15, 20 ]

def binomial(n, k):
    k = min(k, n-k)
    res = 1
    for i in range(1, k+1): res = res * (n - k + i) / i
    return res

for i, t in enumerate(tests):
    with open("T%d.in" % i, 'w') as f: f.write('%d\n' % t)
    with open("T%d.out" % i, 'w') as f:
        for x in range(t):
            for y in range(x+1):
                if y != 0: f.write(' ')
                f.write('%d' % binomial(x, y))
            f.write('\n')

