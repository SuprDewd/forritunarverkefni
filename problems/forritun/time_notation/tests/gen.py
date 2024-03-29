tests = [
    ("0 0", "12:00 AM"),
    ("0 1", "12:01 AM"),
    ("0 59", "12:59 AM"),
    ("1 0", "1:00 AM"),
    ("1 15", "1:15 AM"),
    ("8 0", "8:00 AM"),
    ("11 59", "11:59 AM"),
    ("12 0", "12:00 PM"),
    ("12 5", "12:05 PM"),
    ("12 59", "12:59 PM"),
    ("13 0", "1:00 PM"),
    ("13 9", "1:09 PM"),
    ("15 43", "3:43 PM"),
    ("18 12", "6:12 PM"),
    ("23 0", "11:00 PM"),
    ("23 59", "11:59 PM")
]

for i, t in enumerate(tests):
    with open("T%d.in" % i, 'w') as f: f.write('%s\n' % t[0])
    with open("T%d.out" % i, 'w') as f: f.write('%s\n' % t[1])

