ts = [ 0, 1, 2, 3, 5, 100, 1232, -32, -5234, -5434, -1, -2, -3 ]

for i, t in enumerate(ts):
    with open('T%d.in' % i, 'w') as f: f.write('%d\n' % t)
    with open('T%d.out' % i, 'w') as f: f.write('%d\n' % (t*t))

