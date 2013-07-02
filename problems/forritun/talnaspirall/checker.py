#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        o_lines = obtained.strip().split('\n')
        e_lines = obtained.strip().split('\n')

        if len(o_lines) != len(e_lines): return False

        for (a, b) in zip(o_lines, e_lines):
            a = re.sub(' +', ' ', a.strip().replace('\t', ' '))
            b = re.sub(' +', ' ', b.strip().replace('\t', ' '))

            if a != b:
                return False

        return True
    except ValueError, ex:
        return False
