tests = [ (50, 1.50), (60, 1.51), (62, 1.64), (113, 2.13), (45, 1.32), (83, 1.62) ]

for i, (w, h) in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write('%d\n%0.2f\n' % (w, h))
    with open('T%d.out' % i, 'w') as f: f.write('%0.2f\n' % (w / (h * h)))
