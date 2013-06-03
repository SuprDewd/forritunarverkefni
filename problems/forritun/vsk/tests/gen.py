tests = [ 0, 10, 100, 233, 692, 1000, 15200, 7980, 17000 ]

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d\n' % t)
    with open('T%d.out' % i, 'w') as f: f.write('%f\n' % (t * 1.255))
