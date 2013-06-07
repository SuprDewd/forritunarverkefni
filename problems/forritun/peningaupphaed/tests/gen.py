import random

tests = 10
for t in range(tests):
    a = random.randint(0, 30) if random.randint(0, 4) > 0 else 0
    b = random.randint(0, 30) if random.randint(0, 4) > 0 else 0
    c = random.randint(0, 30) if random.randint(0, 4) > 0 else 0

    with open('T%d.in' % t, 'w') as f: f.write('%d\n%d\n%d\n' % (a, b, c))
    with open('T%d.out' % t, 'w') as f: f.write('%d\n' % (5000 * a + 1000 * b + 500 * c))
