#!/usr/bin/python2
import re

def check(obtained, expected):
    obtained = re.sub(r'[ \t]+', ' ', obtained).strip().split('\n')
    expected = re.sub(r'[ \t]+', ' ', expected).strip().split('\n')
    if len(obtained) != len(expected): return False
    for a, b in zip(obtained, expected):
        a = a.strip()
        b = b.strip()
        if a != b:
            return False
    return True
