# coding: utf8

tests = [
    [1, 2, 3, 4, 5],
    [1, 2, 4, 3, 5],
    [2, 4, 10, 9, 8],
    [2, 4, 8, 9, 10],
    [100, 101, 102, 103, 104],
    [1001, 2002, 2001, 2003, 2004],
    [10, 9, 8, 7, 6],
    [5, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1],
    [1, 3, 2, 4, 5],
]

for i, t in enumerate(tests):
    with open('T%d.in' % i, 'w') as f: f.write(' '.join(map(str, t)) + '\n')
    with open('T%d.out' % i, 'w') as f: f.write(('hækkandi röð' if all(map(lambda (x,y): x<y, zip(t, t[1:]))) else 'ekki hækkandi röð') + '\n')
