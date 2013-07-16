#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        expected = expected.strip().split('\n')
        obtained = obtained.strip().split('\n')

        if len(expected) != len(obtained): return False

        return all( re.sub(' +', ' ', a.strip()) == re.sub(' +', ' ', b.strip()) for a, b in zip(expected, obtained) )
    except ValueError, ex:
        return False
