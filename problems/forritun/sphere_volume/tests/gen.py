import math
ts = [0.0, 1.0, 1.5, 3.5, 0.5, 0.7, 3.1415]

for i, t in enumerate(ts):
    with open('T%d.in' % i, 'w') as f: f.write('%f\n' % t)
    with open('T%d.out' % i, 'w') as f: f.write('%f\n' % (3.0 / 4.0 * math.pi * pow(t/2.0, 3)))

