#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        expected = float(re.sub(r'\s', '', expected))
        obtained = float(re.sub(r'\s', '', obtained))
        return abs(expected - obtained) < 0.001
    except ValueError, ex:
        return False
