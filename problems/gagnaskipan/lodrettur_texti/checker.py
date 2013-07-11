#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        o_lines = obtained.rstrip().split('\n')
        e_lines = expected.rstrip().split('\n')

        if len(o_lines) != len(e_lines): return False

        return all([ a.rstrip() == b.rstrip() for a, b in zip(o_lines, e_lines) ])
    except:
        return False
