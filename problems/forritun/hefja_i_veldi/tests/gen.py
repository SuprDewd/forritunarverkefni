import math
tests = [ (10, 4), (10, -4), (15, -1), (1, 4), (0, 3), (1, -2), (-1, 2), (-1, 3), (-1, 0), (13, 2), (-13, 2), (13, 3), (-13, 3), (-5, -6) ]

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d %d\n' % tuple(t))
    with open('T%d.out' % i, 'w') as f: f.write('%f\n' % math.pow(t[0], t[1]))

