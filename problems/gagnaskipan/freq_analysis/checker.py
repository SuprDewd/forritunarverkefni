#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        o_lines = obtained.strip().split('\n')
        e_lines = expected.strip().split('\n')

        if len(o_lines) != len(e_lines): return False

        for a, b in zip(o_lines, e_lines):
            a = a.strip()
            b = b.strip()
            assert b[-1] == '%'
            if a[-1] != '%': return False
            a = a[:-1].split(' ')
            b = b[:-1].split(' ')

            assert len(a) == len(b)

            if a[0] != b[0]: return False

            if abs(float(a[1]) - float(b[1])) > 1e-1: return False

        return True
    except:
        return False
