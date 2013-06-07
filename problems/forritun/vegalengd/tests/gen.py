tests = [ 0, 1, 2, 3, 4, 8, 10, 12, 15, 20 ]

for i, t in enumerate(tests):
    with file('T%d.in' % i, 'w') as f: f.write('%d\n' % t)
    with file('T%d.out' % i, 'w') as f: f.write('%d\n' % (10 * t * t / 2))
