# coding: utf8
tests = [ (10, 3), (3, 3), (34234, 34234), (3, 10), (213, 1231), (643, 24), (0, 0), (-313, 213), (-4, -53), (-4, -4) ]

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d %d\n' % tuple(t))
    with open('T%d.out' % i, 'w') as f: f.write('%s\n' % ("minni" if t[0] < t[1] else "stærri" if t[0] > t[1] else "jafnar"))
