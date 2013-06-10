import random
tests = [ 10, 100 ]

for i, test in enumerate(tests):
    with open("T%d.in" % i, 'w') as fi, open("T%d.out" % i, 'w') as fo:
        fi.write("%d\n" % test)
        for j in range(test):
            a, b = random.randint(0, 10000), random.randint(0, 10000)
            fi.write("%d %d\n" % (a, b))
            fo.write("%d\n" % abs(a - b))

