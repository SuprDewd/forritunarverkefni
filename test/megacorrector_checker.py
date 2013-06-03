#!/usr/bin/python2
import corrector

def main(checker_file, has_error=False):

    res = corrector.Result(corrector_result=corrector.CORR_OK)

    try:
        sys.path.append(os.path.dirname(checker_file))
        checker = __import__(os.path.basename(checker_file).split('.')[0])

        if checker.check(corrector.obtained(), corrector.expected()):
            res.classification = corrector.ACCEPTED if not has_error else corrector.ACCEPTED_WITH_ERRORS
        else:
            res.classification = corrector.WRONG_ANSWER

    except Exception, ex:
        print(ex)
        res.classification = corrector.REQUIRES_REEVALUATION

    return res
