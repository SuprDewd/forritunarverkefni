import random

tests = 10
for t in range(tests):
    nums = [ random.randint(0 if t == 0 else -1000, 0 if t == 1 else 1000) for _ in range(10) ]
    with open('T%d.in' % t, 'w') as f: f.write('\n'.join(map(str, nums)) + '\n')
    with open('T%d.out' % t, 'w') as f: f.write('%d\n%d\n%d\n' % (sum([ n for n in nums if n > 0 ]), len([ n for n in nums if n > 0 ]), len([ n for n in nums if n <= 0 ]) ))
