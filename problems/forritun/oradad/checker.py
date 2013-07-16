#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        o_lines = obtained.strip().split('\n')
        e_lines = expected.strip().split('\n')

        if len(o_lines) != len(e_lines): return False

        o_vals = map(int, o_lines[0].strip().split(' '))
        e_vals = map(int, e_lines[0].strip().split(' '))

        if sorted(o_vals) != sorted(e_vals): return False

        return len({ x < y for (x, y) in zip(o_vals, o_vals[1:]) }) == 2
    except:
        return False

