#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        expected = re.sub(r'\s', '', expected)
        obtained = re.sub(r'\s', '', obtained)
        expected_f = float(expected)
        obtained_f = float(obtained)
        return re.match(r'^\d+\.\d{2}$', obtained) and abs(expected_f - obtained_f) <= 0.019
    except ValueError, ex:
        return False
