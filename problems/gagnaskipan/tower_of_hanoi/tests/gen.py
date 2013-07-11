ts = [ 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 15, 16 ]

for i, t in enumerate(ts):
    with open('T%d.in' % i, 'w') as f: f.write('%d\n' % t)
    with open('T%d.out' % i, 'w') as f:
        pegs = [ range(t), [], [] ]
        small = 0
        for j in range((1<<t) - 1):
            if j % 2 == 0:
                x = small
                y = (small + (1 if t % 2 == 0 else -1) + 3) % 3
                small = y
            else:
                [(_, y), (_, x)] = sorted([ (b,a) for a,b in enumerate([ p[-1] if p else -1 for p in pegs ]) ])[:-1]

            f.write('Move from %s to %s\n' % (chr(ord('A') + x), chr(ord('A') + y)))
            pegs[y].append(pegs[x].pop())

        assert pegs[-1] == range(t)

