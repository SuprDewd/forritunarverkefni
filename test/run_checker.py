#!/usr/bin/python2
import sys
import os

RET_AC = 0
RET_WA = 1
RET_ERR = 2

def main(checker_file, obtained_file, expected_file):
    sys.path.append(os.path.dirname(checker_file))
    checker = __import__(os.path.basename(checker_file).split('.')[0])

    with open(obtained_file, 'r') as obt_f, open(expected_file, 'r') as exp_f:
        obtained = obt_f.read()
        expected = exp_f.read()

    try:
        if checker.check(obtained, expected):
            return RET_AC
        else:
            print("Expected:")
            print(expected)
            print("Obtained:")
            print(obtained)
            return RET_WA
    except Exception, ex:
        print(ex)
        return RET_ERR

if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
