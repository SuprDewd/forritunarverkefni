#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        o_lines = obtained.strip().split('\n')
        e_lines = expected.strip().split('\n')

        if len(o_lines) != len(e_lines): return False
        if o_lines[0].strip() != e_lines[0].strip(): return False

        vals = o_lines[1].split(' ')
        if not all([ len(v) == 2 for v in vals ]): return False

        vals = [ (ord(v[0]) - ord('a'), ord(v[1]) - ord('1')) for v in vals ]
        for (x1, y1), (x2, y2) in zip(vals, vals[1:]):
            a = abs(x1 - x2)
            b = abs(y1 - y2)
            if a > b: a, b = b, a
            if a != 1 or b != 2: return False

        return True
    except:
        return False
