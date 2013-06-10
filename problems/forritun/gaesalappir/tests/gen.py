# coding: utf8
import random
import string
tests = 10

for t in range(tests):
    cnt = random.randint(1, 1000)
    s = ''.join([ random.choice(string.ascii_letters) for i in range(cnt) ])
    with open("T%d.in" % t, 'w') as f: f.write('%s\n' % s)
    with open("T%d.out" % t, 'w') as f: f.write('ég las inn "%s"\n' % s)
