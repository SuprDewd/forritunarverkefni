#!/usr/bin/python2
import re

def check(obtained, expected):
    try:
        o_lines = obtained.strip().split('\n')
        e_lines = expected.strip().split('\n')

        if len(o_lines) != len(e_lines): return False

        if len(e_lines) == 1:
            return e_lines[0].strip() == o_lines[0].strip()

        oa = o_lines[0].strip().split(' ')[-1]
        ob = o_lines[1].strip().split(' ')[-1]
        oc = o_lines[2].strip().split(' ')[-1]

        ea = e_lines[0].strip().split(' ')[-1]
        eb = e_lines[1].strip().split(' ')[-1]
        ec = e_lines[2].strip().split(' ')[-1]

        if len(oa) != len(ea): return False
        if len(ob) != len(eb): return False
        if len(oc) != len(ec): return False

        if int(oa) + int(ob) != int(oc): return False
        if (oa[0] == '0' and len(oa) != 1) or (ob[0] == '0' and len(ob) != 1) or (oc[0] == '0' and len(oc) != 1): return False

        assoc = {}

        for (x, y) in zip(oa + ob + oc, ea + eb + ec):
            if y in assoc:
                if x != assoc[y]:
                    return False
            else:
                assoc[y] = x

        return True
    except:
        return False
