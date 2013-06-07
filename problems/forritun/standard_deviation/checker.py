#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        expected = float(re.sub(r'\s', '', expected))
        obtained = float(re.sub(r'\s', '', obtained))
        return abs(expected - obtained) < 1e-3
    except ValueError, ex:
        return False
