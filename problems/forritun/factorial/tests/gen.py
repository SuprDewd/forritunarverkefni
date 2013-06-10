tests = range(1, 13)

def fac(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d\n' % t)
    with open('T%d.out' % i, 'w') as f: f.write('%d\n' % fac(t))

