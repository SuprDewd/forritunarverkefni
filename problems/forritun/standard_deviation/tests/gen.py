import random
import math
tests = 9

for i in range(tests):
    n = random.randint(1, 10)
    nums = [ float(str(random.random() * 200 - 10)) for _ in range(n) ]
    avg = sum(nums) / n
    stdev = math.sqrt(sum([ math.pow(xi - avg, 2.0) for xi in nums ]) / n)
    with open('T%d.in' % i, 'w') as f: f.write('\n'.join(map(str, [n] + nums)) + '\n')
    with open('T%d.out' % i, 'w') as f: f.write('%f\n' % stdev)
