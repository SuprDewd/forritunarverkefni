coins = [1, 5, 10, 50, 100, 500, 1000, 5000]
tests = [1, 5, 10, 50, 100, 500, 1000, 5000, 2, 3, 4, 6, 7, 8, 9, 501, 506, 599, 9999, 10000, 15532, 4324, 5643, 4355, 8775, 15257]

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d\n' % t)
    with open('T%d.out' % i, 'w') as f:
        left = t
        for c in reversed(sorted(coins)):
            if left / c > 0:
                f.write('%d x %d kr.\n' % (left / c, c))
                left %= c
