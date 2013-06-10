tests = [ (1, 5), (1, 100), (90, 100), (20, 80) ]

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    if n < 25: return True
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d %d\n' % tuple(t))
    with open('T%d.out' % i, 'w') as f:
        for n in range(t[0], t[1]+1):
            if is_prime(n):
                f.write('%d\n' % n)

