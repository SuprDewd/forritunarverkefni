import re

def check(obtained, expected):
    try:
        o_lines = obtained.strip().split('\n')
        e_lines = expected.strip().split('\n')
        if len(o_lines) != len(e_lines):
            return False
        else:
            for (a, b,) in zip(o_lines, e_lines):
                asp = a.strip().split(' ')
                bsp = b.strip().split(' ')
                if len(asp) != len(bsp):
                    return False
                if asp[0].strip() != bsp[0].strip():
                    return False
                if abs(float(asp[1].strip()) - float(bsp[1].strip())) > 0.1:
                    return False

            return True
    except ValueError as ex:
        return False

