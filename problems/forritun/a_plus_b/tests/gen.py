tests = [ (0, 0), (1, -1), (-3, 5), (1230, 12), (83, 323), (9933, 12383), (-2321, 2332),  (-231, -2323), (11322, 0), (0, 2343), (0, -21312) ]

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d\n%d\n' % (t[0], t[1]))
    with open('T%d.out' % i, 'w') as f: f.write('%d\n' % (t[0] + t[1]))
