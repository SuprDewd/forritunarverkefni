#!/usr/bin/python2
import re

def check(obtained, expected):
    try:

        obtained = obtained.strip().split('\n')
        expected = expected.strip().split('\n')

        if len(obtained) != len(expected): return False
        if int(obtained[1].strip()) != int(expected[1].strip()): return False

        expected = float(expected[0].strip())
        obtained = float(obtained[0].strip())
        return abs(expected - obtained) <= 0.001
    except ValueError, ex:
        return False
