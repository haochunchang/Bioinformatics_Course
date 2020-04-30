import sys
import unittest
from os.path import dirname
from unittest import TextTestRunner
from importlib import import_module

ID = sys.argv[1]


class KnownGood(unittest.TestCase):
    def __init__(self, inputs, output):
        super(KnownGood, self).__init__()
        self.input = inputs
        self.output = output

    def runTest(self):
        self.assertEqual(self.input, self.output)


class PrivateCases(KnownGood):
    def __init__(self, inputs, outputs):
        super(PrivateCases, self).__init__(inputs, outputs)


class PublicCases(KnownGood):
    def __init__(self, inputs, outputs):
        super(PublicCases, self).__init__(inputs, outputs)


class ProblemGrader:
    def __init__(self, pid):
        self.pid = pid

    def grade_single_problem(self):
        """
        Test and grade a single problem
        pid: problem id
        """
        pid = self.pid
        DIR = join("students", ID, "problem{}".format(pid))
        load_data = import_module("problem{}.load".format(pid)).load_data
        load_answer = import_module("problem{}.load".format(pid)).load_answer

        public_output = join(DIR, "pub_out.txt")
        private_output = join(DIR, "pri_out.txt")
        script_path = join(DIR, "{}_problem{}.py".format(ID, pid))

        import subprocess

        cmd = "python {} {}/public_data.txt {}".format(script_path, DIR, public_output)
        subprocess.run(cmd.split(), check=True, timeout=60)

        cmd = "python {} problem{}_private.txt {}".format(
            script_path, self.pid, private_output
        )
        subprocess.run(cmd.split(), check=True, timeout=60)

        suite = self.public_suite(public_output, load_data, load_answer)
        public = TextTestRunner(verbosity=0).run(suite)
        pb_score = self.calculate_grade(public)

        suite = self.private_suite(private_output, load_data, load_answer)
        private = TextTestRunner(verbosity=0).run(suite)
        pr_score = self.calculate_grade(private)

        total_score = pb_score * 0.7 + pr_score * 0.3
        # print("Problem {}, {:.2f}".format(pid, total_score))
        # print("Public,{:.2f}".format(pb_score))
        # print("Private,{:.2f}".format(pr_score))
        return pid, total_score

    def private_suite(self, filepath, load_data, load_answer):

        suite = unittest.TestSuite()

        test_ans = load_data("problem{}_private.txt".format(self.pid))
        answers = load_answer(filepath)
        suite.addTests(
            PrivateCases(inputs, output) for inputs, output in zip(answers, test_ans)
        )
        return suite

    def public_suite(self, filepath, load_data, load_answer):

        dirs = dirname(filepath)
        suite = unittest.TestSuite()

        test_ans = load_data(join(dirs, "public_data.txt"))
        answers = load_answer(filepath)
        suite.addTests(
            PublicCases(inputs, output) for inputs, output in zip(answers, test_ans)
        )
        return suite

    def calculate_grade(self, result):
        """
        result: TestResult object
        """
        assert isinstance(result, unittest.TestResult)
        npub = result.testsRun
        nfail = len(result.failures)
        nerr = len(result.errors)
        score = (npub - nfail - nerr) / npub
        return score


if __name__ == "__main__":

    from os.path import join

    print("ID: {}".format(ID))
    scores = [ID]
    for pid in range(1, 5):
        grader = ProblemGrader(pid)
        try:
            pid, score = grader.grade_single_problem()
        except Exception as e:
            print(e)
            score = 0
        scores.append(score)
    total_score = scores[1] * 0.3 + scores[2] * 0.3 + scores[3] * 0.4 + scores[4] * 0.15
    total_score = min(1.0, total_score) * 100

    scores = [str(x) for x in scores] + [str(total_score)]
    with open(sys.argv[2], "a") as f:
        f.write(", ".join(scores) + "\n")
