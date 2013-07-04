import math
ts = [ (3.4, 8.2), (6.3, 5.0), (5.0, 1.0), (5.0, 5.0), (25.0, 1000.0) ]

for i, t in enumerate(ts):
    with open('T%d.in' % i, 'w') as f: f.write('%f %f\n' % t)
    with open('T%d.out' % i, 'w') as f: f.write('%f\n' % (math.log(t[1]) / math.log(t[0])))

