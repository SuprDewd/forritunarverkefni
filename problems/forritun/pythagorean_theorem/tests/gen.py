from math import sqrt, pow

ts = [ (3.0, 4.0), (1.0, 2.0), (5.0, 12.0), (6.0, 4.0), (3.243, 8.32), (3.13, 4.442) ]

for i, t in enumerate(ts):
    with open('T%d.in' % i, 'w') as f: f.write('%f %f\n' % t)
    with open('T%d.out' % i, 'w') as f: f.write('%f\n' % sqrt(pow(t[0], 2) + pow(t[1], 2)))

