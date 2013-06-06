import math
tests = range(2, 17) + [ 100, 110, 200, 349 ]

for i, t in enumerate(tests):
    with file("T%d.in" % i, 'w') as f: f.write('%d\n' % t)
    with file("T%d.out" % i, 'w') as f: f.write('%f\n' % math.sqrt(t))
