import random
tests = [ (0, 0), (0, 10), (10, 0), (5, 5), (100, 10), (10, 100), (1000, 1000), (15, 13), (1, 1), (1, 23), (23, 1) ]

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as fi, open('T%d.out' % i, 'w') as fo:
        for j in range(t[0]):
            r = random.randint(0, 1000)
            if r == 42: r = 1
            fi.write('%d\n' % r)
            fo.write('%d\n' % r)

        fi.write('%d\n' % 42)
        fo.write('%d\n' % 42)

        for j in range(t[1]):
            r = random.randint(0, 1000)
            fi.write('%d\n' % r)
