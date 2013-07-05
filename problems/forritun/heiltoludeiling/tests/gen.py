import random

def cdiv(x, y):
    return abs(x) / abs(y) * cmp(x, 0) * cmp(y, 0)

ts = 10
for i in range(ts):
    a = random.randint(-1000, 1000)
    b = random.randint(-1000, 1000)

    with open('T%d.in' % i, 'w') as f: f.write('%d %d\n' % (a, b))
    with open('T%d.out' % i, 'w') as f: f.write('%f\n%d\n' % (float(a)/float(b), cdiv(a, b)))

