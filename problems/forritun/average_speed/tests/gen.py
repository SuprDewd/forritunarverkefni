import random
ts = 11

def format(d):
    return '%02d:%02d:%02d' % ((d/60/60)%60, (d/60)%60, d%60)

for i in range(ts):
    cnt = random.randint(1, 500)
    at = 0
    total = 0
    speed = 0

    with open('T%d.in' % i, 'w') as fi, open('T%d.out' % i, 'w') as fo:
        for j in range(cnt):
            if random.randint(0, 1) == 0:
                add = random.randint(1, 500)
                at += add
                sp = random.randint(0, 200)
                fi.write('%s %d\n' % (format(at), sp))
                total += add * speed / 60.0 / 60.0
                speed = sp
            else:
                add = random.randint(0, 500)
                at += add
                fi.write('%s\n' % format(at))
                total += add * speed / 60.0 / 60.0
                fo.write('%s %0.2f km\n' % (format(at), total))

