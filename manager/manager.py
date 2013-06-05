#!/usr/bin/python2
import xml_parser
from xml_parser import parse_xml
from optparse import OptionParser
import os
import tempfile
import string
import random
import shutil
from zipfile import ZipFile

PROBLEM_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'problems'))
CONTEST_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'contests'))

TEXT_ELEMS = ['description', 'solution', 'checker', 'input', 'output', 'explanation']

def get_contents(file, dir=None):
    if dir: file = os.path.join(dir, file)
    with open(file, 'r') as f:
        return f.read()

def set_contents(file, s, dir=None):
    if dir: file = os.path.join(dir, file)
    with open(file, 'w') as f:
        f.write(s)

class Problem:

    class _Code:
        def __init__(self, code=None, language=None):
            self.code = code
            self.language = language

    class Solution(_Code):
        def __init__(self, code=None, language=None):
            Problem._Code.__init__(self, code, language)

    class Checker(_Code):
        def __init__(self, code=None, language=None):
            Problem._Code.__init__(self, code, language)

    class Test:
        def __init__(self, input=None, output=None, timelimit=None, memorylimit=None, example=None, explanation=None):
            self.input = input
            self.output = output
            self.timelimit = timelimit
            self.memorylimit = memorylimit
            self.example = example
            self.explanation = explanation

    def __init__(self, id, description=None, solution=None, checker=None, tests=None):
        self.id = self.name = id
        self.description = None
        self.solution = None
        self.checker = None
        self.tests = tests if tests else []

class Contest:
    def __init__(self, id, name=None, email=None, problems=None):
        self.id = id
        self.name = name
        self.email = email
        self.problems = problems if problems else []

def _convert_timelimit_str(s):
    i = 0
    while i < len(s) and s[i].isdigit(): i += 1
    amount = int(s[0:i])
    suffix = s[i:]
    if suffix == 's': amount *= 1000
    elif suffix == 'ms': amount *= 1
    elif suffix == 'm': amount *= 60 * 1000
    return amount

def _convert_memorylimit_str(s):
    i = 0
    while i < len(s) and s[i].isdigit(): i += 1
    amount = int(s[0:i])
    suffix = s[i:]
    if suffix == 'KB': amount *= 1024
    elif suffix == 'MB': amount *= 1024**2
    elif suffix == 'GB': amount *= 1024**3
    return amount

def _parse_problem(pid, tree, p_dir):

    assert len(tree) == 1
    assert tree[0].tag == 'problem'

    problem = Problem(pid)
    if 'name' in tree[0].attr:
        problem.name = tree[0].attr['name']

    for n1 in tree[0].children:
        if n1.tag == 'description':
            if 'include' in n1.attr:
                problem.description = get_contents(n1.attr['include'], p_dir)
            else:
                problem.description = n1.children
        elif n1.tag == 'solution':
            problem.solution = Problem.Solution()
            if 'language' in n1.attr:
                problem.solution.language = n1.attr['language']
            if 'include' in n1.attr:
                if 'language' not in n1.attr:
                    problem.solution.language = 'C++' if n1.attr['include'].endswith('.cpp') else \
                                               'Python 3' if n1.attr['include'].endswith('.py3') else \
                                               'Python 2' if n1.attr['include'].endswith('.py') else None
                problem.solution.code = get_contents(n1.attr['include'], p_dir)
            else:
                problem.solution.code = n1.children[0]
        elif n1.tag == 'checker':
            problem.checker = Problem.Checker()
            if 'language' in n1.attr:
                problem.checker.language = n1.attr['language']
            if 'include' in n1.attr:
                if 'language' not in n1.attr:
                    problem.checker.language = 'C++' if n1.attr['include'].endswith('.cpp') else \
                                               'Python 3' if n1.attr['include'].endswith('.py3') else \
                                               'Python 2' if n1.attr['include'].endswith('.py') else None
                problem.checker.code = get_contents(n1.attr['include'], p_dir)
            else:
                problem.checker.code = n1.children[0]
        elif n1.tag == 'tests':
            timelimit = n1.attr.get('timelimit')
            memorylimit = n1.attr.get('memorylimit')
            for n2 in n1.children:
                if n2.tag == 'test':
                    test = Problem.Test()
                    problem.tests.append(test)
                    if 'input_include' in n2.attr:
                        test.input = get_contents(n2.attr['input_include'], p_dir)
                    if 'output_include' in n2.attr:
                        test.output = get_contents(n2.attr['output_include'], p_dir)
                    if 'explanation_include' in n2.attr:
                        test.explanation = get_contents(n2.attr['explanation_include'], p_dir)
                    test.timelimit = n2.attr.get('timelimit') or timelimit
                    if test.timelimit: test.timelimit = _convert_timelimit_str(test.timelimit)
                    test.memorylimit = n2.attr.get('memorylimit') or memorylimit
                    if test.memorylimit: test.memorylimit = _convert_memorylimit_str(test.memorylimit)
                    test.example = n2.attr.get('example', 'False') == 'True'
                    for n3 in n2.children:
                        if n3.tag == 'input':
                            test.input = ''.join(map(str, n3.children))
                        elif n3.tag == 'output':
                            test.output = ''.join(map(str, n3.children))
                        elif n3.tag == 'explanation':
                            test.explanation = ''.join(map(str, n3.children))

    return problem


def load_problem(pid):

    p_dir = None
    for loc in [ os.path.join(PROBLEM_DIR, pid, 'problem.xml'),
                 os.path.join(PROBLEM_DIR, pid + '.xml'),
                 os.path.join(PROBLEM_DIR, pid, pid + '.xml') ]:
        if os.path.exists(loc):
            p_dir = os.path.dirname(loc)
            tree = parse_xml(get_contents(loc), TEXT_ELEMS)
            break

    if not p_dir:
        raise Exception('Problem not found')

    return _parse_problem(pid, tree, p_dir)


def load_contest(cid):

    c_dir = None
    for loc in [ os.path.join(CONTEST_DIR, cid, 'contest.xml'),
                 os.path.join(CONTEST_DIR, cid + '.xml'),
                 os.path.join(CONTEST_DIR, cid, cid + '.xml') ]:
        if os.path.exists(loc):
            c_dir = os.path.dirname(loc)
            tree = parse_xml(get_contents(loc), TEXT_ELEMS)
            break

    if not c_dir:
        raise Exception('Contest not found')

    assert len(tree) == 1
    assert tree[0].tag == 'contest'

    contest = Contest(cid)
    if 'name' in tree[0].attr:
        contest.name = tree[0].attr['name']

    if 'email' in tree[0].attr:
        contest.email = tree[0].attr['email']

    for n1 in tree[0].children:
        if n1.tag == 'problem':
            if 'include' in n1.attr:
                problem = load_problem(n1.attr['include'])
                contest.problems.append(problem)
                if 'name' in n1.attr:
                    problem.name = n1.attr['name']
            else:
                problem = _parse_problem(n1.attr['id'], n1, c_dir)
                contest.problems.append(problem)

    return contest


def description_to_html(desc):
    # def to_html(n):
    #     if isinstance(n, xmlparser.Text):
    #         return str(n)
    #     else:
    #         return str(n)

    return str(''.join(map(str, desc)))

def export_problem(problem, path, add_xmlns=True, add_xml_header=True, xml_path=None, problem_seq_name=None, write_content_xml=True):
    xml_path = xml_path if xml_path else ''

    description_file = 'description.html'
    solution_file = 'solution' + ('.cpp' if problem.solution.language.title() == 'C++' else
                                  '.py3' if problem.solution.language.title().startswith('Python 3') else
                                  '.py' if problem.solution.language.title().startswith('Python') else
                                  '')
    checker_file = 'checker' +  ('.cpp' if problem.solution.language.title() == 'C++' else
                                  '.py3' if problem.solution.language.title().startswith('Python 3') else
                                  '.py' if problem.solution.language.title().startswith('Python') else
                                  '')

    set_contents(description_file, description_to_html(problem.description), path)
    set_contents(solution_file, problem.solution.code, path)

    if problem.checker:
        set_contents(checker_file, problem.checker.code, path)

    if not os.path.exists(os.path.join(path, 'tests')):
        os.mkdir(os.path.join(path, 'tests'))
    tests = ""
    timelimit = None
    for i, t in enumerate(problem.tests):
        if not timelimit:
            timelimit = t.timelimit
        elif t.timelimit:
            timelimit = max(timelimit, t.timelimit)
        if not os.path.exists(os.path.join(path, 'tests/T%d' % i)):
            os.mkdir(os.path.join(path, 'tests/T%d' % i))
        set_contents('tests/T%d/input' % i, t.input, path)
        set_contents('tests/T%d/output' % i, t.output, path)
        tests += """
          <Test xml:id="%(test_path)s.T%(i)d"
                    Fatal=""
                    Warning=""
                    args=""
                    input="input"
                    output="output"
                    context="context"
                    Points=""
                    Feedback=""
                    Show=""/>
        """ % {'i': i, 'test_path': '.'.join([ part for part in [xml_path, problem_seq_name, 'tests'] if part ]) }

    xml = ""
    if add_xml_header:
        xml += """<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
"""

    xml += """<Problem %(xmlns)s
          Fatal=""
          Warning=""
          Name="%(id)s"
          Color=""
          Title="%(name)s"
          Difficulty=""
          Type=""
          Description="%(description)s"
          PDF=""
          Program="%(solution)s"
          Environment="Environment"
          Timeout="%(timelimit)d"
          Static_corrector="%(static_corrector)s"
          Dynamic_corrector="%(dynamic_corrector)s"
          Original_location=""
          Start=""
          Stop="">
     <Images xml:id="%(img_path)s"
               Fatal=""
               Warning=""
               Image=""/>
     <Tests xml:id="%(tests_path)s"
               Fatal=""
               Warning=""
               Definition="Definition">
          %(tests)s
     </Tests>
</Problem>
""" % { 'xmlns': ('xmlns="http://www.ncc.up.pt/mooshak/"' if add_xmlns else '') + " " + ("""xml:id="%s" """ % '.'.join([xml_path, problem_seq_name]) if problem_seq_name else ""),
        'img_path': '.'.join([ part for part in [xml_path, problem_seq_name, 'tests'] if part ]),
        'tests_path': '.'.join([xml_path, 'images']) if xml_path else 'images',
        'id': problem_seq_name,
        'name': xml_parser.encode_entities(problem.name),
        'description': description_file,
        'solution': solution_file,
        'timelimit': (timelimit or 60*1000) / 1000,
        'static_corrector': "/usr/bin/python $home/correctors/megacorrector.py !cppcheck_corrector korea_corrector('$home/bin/nsiqcppstyle/mooshak_filter.txt') vera_corrector('mooshak')",
        'dynamic_corrector': "/usr/bin/python $home/correctors/megacorrector.py tle_corrector valgrind_corrector regex_corrector(True)",
        'tests': tests
        }

    # TODO: Finish correctors/checkers

    if write_content_xml:
        set_contents('Content.xml', xml, path)

    return xml

def export_contest(contest, path):

    if not os.path.exists(os.path.join(path, 'problems')):
        os.mkdir(os.path.join(path, 'problems'))
    problems = ""
    for i, p in enumerate(contest.problems):
        prob_id = "%03d_%s" % (i, p.id.replace('/', '_'))
        prob_dir = os.path.join(path, 'problems', prob_id)
        if not os.path.exists(prob_dir):
            os.mkdir(prob_dir)
        problems += export_problem(p, prob_dir, add_xmlns=False, add_xml_header=False, xml_path="problems", problem_seq_name=prob_id, write_content_xml=False)

    xml = """<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<Contest xmlns="http://www.ncc.up.pt/mooshak/"
          Type=""
          Status="running"
          Fatal=""
          Warning=""
          Designation="%(name)s"
          Organizes=""
          Email="%(email)s"
          Open="1360877400"
          Start="1360877400"
          Stop=""
          Close=""
          HideListings=""
          Policy="icpc"
          Virtual="no"
          Register="no"
          Service="none"
          Notes=""
          challenge="problems">
     <Groups xml:id="groups"
               Fatal=""
               Warning=""
               Printer=""
               Team_template=""
               Person_template=""
               Password_template=""
               Config="">
          <Group xml:id="groups.%(group)s"
                    Fatal=""
                    Warning=""
                    Designation="%(group)s"
                    Acronym="%(group)s"
                    Color="Black"
                    Flag="00"
                    Authentication=""
                    Basic="">
          </Group>
     </Groups>
     <Problems xml:id="problems"
               Fatal=""
               Warning=""
               Presents="list">
            %(problems)s
     </Problems>
     <Submissions xml:id="submissions"
               Fatal=""
               Warning=""
               Default_state="final"
               Multiple_accepts="yes"
               Run_all_tests="yes"
               Show_own_code="yes"
               Give_feedback="report"
               Show_errors="{} Accepted {Presentation Error} {Wrong Answer} {Output Limit Exceeded} {Memory Limit Exceeded} {Time Limit Exceeded} {Invalid Function} {Runtime Error} {Compile Time Error} {Invalid Submission} {Program Size Exceeded} {Requires Reevaluation} Evaluating"
               Feedback_delay=""
               Minimum_interval=""
               Maximum_pending="">
     </Submissions>
     <Questions xml:id="questions"
               Active=""
               Forward="">
     </Questions>
     <Printouts xml:id="printouts"
               Active=""
               Printer=""
               Template=""
               Config=""
               List-Pending=""/>
     <Balloons xml:id="balloons"
               List-Pending="">
     </Balloons>

    <Languages xml:id="languages"
          MaxCompFork="100"
          MaxExecFork="100"
          MaxCore="100"
          MaxData="335544320"
          MaxOutput="512000"
          MaxStack="838860800"
          MaxProg="10240000"
          RealTimeout="60"
          CompTimeout="60"
          ExecTimeout="5"
          MinUID="30000"
          MaxUID="60000">
     <Language xml:id="languages.CPP"
               Name="C++"
               Extension="cpp"
               Compiler="gcc"
               Version="2.96"
               Compile="/usr/bin/g++ -Wall -ggdb $file"
               Execute="$home/bin/valgrind_time_limitor 10 --log-file=.valgrind_log --leak-check=full --show-reachable=yes ./a.out"/>
     <Language xml:id="languages.CppSeparateCompilation"
               Name="C++"
               Extension="zip"
               Compiler="gcc"
               Version="2.96"
               Compile="$home/data/contests/gagnaskipan/languages/CppSeparateCompilation/compiler $home/$environment $file"
               Execute="$home/bin/valgrind_time_limitor 10 --log-file=.valgrind_log --leak-check=full --show-reachable=yes ./a.out"
               Omit="^removed .*"/>
        </Languages>
     <Users xml:id="users"/>
</Contest>
""" % { 'name': xml_parser.encode_entities(contest.name),
        'group': 'nem',
        'problems': problems,
        'email': contest.email }

    set_contents('Content.xml', xml, path)

def zip_dir(directory, zip_file):
    with ZipFile(zip_file, 'w') as f:
        for (dirpath, dirnames, filenames) in os.walk(directory):
            for fn in filenames:
                f.write(os.path.join(dirpath, fn), dirpath[len(directory):] + '/' + fn)

def main():
    parser = OptionParser(usage='usage: %prog [options]')
    parser.add_option('-c', '--contest', dest='contest', help='the contest to manage')
    parser.add_option('-p', '--problem', dest='problem', help='the problem to manage', default=None)
    parser.add_option('-d', '--destination', dest='destination', help='the path to export to', default='.')
    (options, args) = parser.parse_args()

    if not options.contest:
        parser.print_help()
        return

    contest = load_contest(options.contest)

    tmp_path = os.path.join(tempfile.gettempdir(), 'manager_' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))

    os.makedirs(tmp_path)
    if options.problem:
        (i, problem) = [ (i, p) for (i, p) in enumerate(contest.problems) if p.id.split('/')[-1] == options.problem.split('/')[-1] ][0]
        output_file = '%03d_%s' % (i, problem.id.replace('/', '_'))
        export_problem(problem, tmp_path)
    else:
        output_file = contest.id.replace('/', '_')
        export_contest(contest, tmp_path)

    ok = True
    output_file += '.zip'
    output_path = os.path.join(options.destination, output_file)
    if os.path.exists(output_path):
        resp = raw_input("%s already exists in specified destination, overwrite? [yN] " % output_file)
        if not resp.lower().startswith('y'):
            print("exiting")
            ok = False

    if ok:
        zip_dir(tmp_path, output_path)

    shutil.rmtree(tmp_path)

if __name__ == '__main__':
    main()
