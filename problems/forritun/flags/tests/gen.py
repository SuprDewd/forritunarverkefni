tests = [1, 10, 15, 2, 20, 25, 3, 30, 35, 4, 40, 41, 42, 43, 44, 45, 5, 6]

mem = {}
def res(n):
    if n == 1: return 2
    if n == 2: return 2
    if n not in mem: mem[n] = res(n-1) + res(n-2)
    return mem[n]

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d\n' % t)
    with open('T%d.out' % i, 'w') as f: f.write('%d\n' % res(t))

