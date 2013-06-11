# coding: utf8
import random
tests = 10

for t in range(tests):
    n = random.randint(0, 10000)
    with open("T%d.in" % t, 'w') as f: f.write('%d\n' % n)
    with open("T%d.out" % t, 'w') as f: f.write('ég las inn "%d"\n' % n)
