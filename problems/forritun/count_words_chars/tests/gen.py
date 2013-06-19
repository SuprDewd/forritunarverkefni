import random
import string

tests = 10
seps = [ '.', ' ', '.' ]

def rand_word(n): return ''.join([ random.choice(string.ascii_letters) for _ in range(n) ])

for t in range(tests):
    with open('T%d.in' % t, 'w') as f:
        n = random.randint(1, 100)
        res = ''
        while n > 0:
            m = random.randint(0, min(n, 10))
            n -= m
            res += random.choice(seps + [''])
            res += rand_word(m)

        m = random.randint(0, 4)
        for _ in range(m):
            res += random.choice(seps + [''])

        f.write(res + '\n')

    with open('T%d.out' % t, 'w') as f:
        def cnt(s, sep):
            if not s: return 0
            if not sep: return 1
            return sum([ cnt(q, sep[1:]) for q in s.split(sep[0]) ])

        f.write('%d words\n' % cnt(res, seps))
        cntz = {}
        for c in res.lower():
            if c in string.ascii_letters:
                cntz.setdefault(c, 0)
                cntz[c] += 1

        for c, cn in sorted(cntz.items()):
            f.write('%d %s\n' % (cn, c))

