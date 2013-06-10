tests = [ -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 100, -101, 321, -123, -13222, 59 ]

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d\n' % t)
    with open('T%d.out' % i, 'w') as f: f.write('%d\n' % abs(t))
