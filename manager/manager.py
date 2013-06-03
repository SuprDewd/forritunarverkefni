from xml_parser import parse_xml
import os

PROBLEM_DIR = os.path.join(os.path.realname(__file__), '..', 'problems')
CONTEST_DIR = os.path.join(os.path.realname(__file__), '..', 'contests')

def get_contents(file):
    with open(file, 'r') as f:
        return f.read()

class Problem:

    class Code:
        def __init__(self, code=None, code_location=None, language=None):
            self.code = code
            self.code_location = code_location
            self.language = language

        def get_code(self):
            if not self.code: self.code = get_contents(self.code_location)
            return self.code

    class Solution(Code):
        def __init__(self, code=None, code_location=None, language=None):
            Code.__init__(self, code, code_location, language)

    class Checker(Code):
        def __init__(self, code=None, code_location=None, language=None):
            Code.__init__(self, code, code_location, language)

    class Test:
        def __init__(self, input=None, output=None, input_location=None, output_location=None):
            self.input = input
            self.output = output
            self.input_location
            self.output_location

        def get_input(self):
            if not self.input: self.input = get_contents(self.input_location)
            return self.input

        def get_output(self):
            if not self.output: self.output = get_contents(self.output_location)
            return self.output

    def __init__(self, id, description=None, description_location=None, solution=None, tests=None):
        self.id = self.name = id
        self.description = None
        self.solution = None
        self.tests = tests if tests else []

    def get_description(self):
        if not self.description: self.description = parse_xml(self.description_location, ['*'])
        return self.description

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
