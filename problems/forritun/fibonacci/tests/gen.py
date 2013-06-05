tests = [1, 2, 3, 5, 10, 11, 12, 20, 25, 30]

def fib(n):
    a, b = 1, 1
    for i in range(1, n): a, b = b, a+b
    return a

for t, test in enumerate(tests):
    with file('T%d.in' % t, 'w') as f: f.write('%d\n' % test)
    with file('T%d.out' % t, 'w') as f: f.write('%d\n' % fib(test))
