from xml_parser import parse_xml
import os

PROBLEM_DIR = os.path.join(os.path.realname(__file__), '..', 'problems')
CONTEST_DIR = os.path.join(os.path.realname(__file__), '..', 'contests')

class Problem:

    class Solution:
        def __init__(self):
            pass

    class Test:
        def __init__(self):
            pass

    def __init__(id):
        self.id = self.name = id
        self.description = None
        self.solution = None
        self.tests = []

def load_problem(pid):

    for loc in [ os.path.join(PROBLEM_DIR, pid, 'problem.xml'),
                 os.path.join(PROBLEM_DIR, pid + '.xml'),
                 os.path.join(PROBLEM_DIR, pid, pid + '.xml') ]:
        if os.path.exists(loc):
            p_dir = os.path.dirname(loc)
            tree = parse_xml(loc, ['description', 'solution', 'input', 'output'])
            break

    if not p_dir:
        raise Exception('Problem not found')

    assert len(tree) == 1
    assert tree[0].tag == 'problem'

    problem = Problem(pid)
    if 'name' in tree[0].attr:
        problem.name = tree[0].attr['name']

    for n1 in tree[0].children:
        # TODO
        pass
