from random import randint
ts = 11

for t in range(ts):
    n = randint(0, 20000)
    with open('T%d.in' % t, 'w') as f: f.write('%d\n' % n)
    with open('T%d.out' % t, 'w') as f: f.write('%d\n' % sum( i for i in range(n) if i % 3 == 0 or i % 5 == 0 ))

