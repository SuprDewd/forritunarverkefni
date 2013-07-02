#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        o_lines = obtained.strip().split('\n')
        e_lines = expected.strip().split('\n')

        if len(o_lines) != len(e_lines): return False

        return all([ a.strip() == b.strip() for a, b in zip(o_lines, e_lines) ])
    except:
        return False
