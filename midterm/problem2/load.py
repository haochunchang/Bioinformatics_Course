"""
Functions for loading testing data
"""


def load_data(filepath):
    test_ans = []
    with open(filepath, "r") as f:
        for line in f:
            rna, ans = line.split(",")
            test_ans.append(ans.rstrip())
    return test_ans


def load_answer(filepath):
    ans = []
    with open(filepath, "r") as f:
        for line in f:
            ans.append(line.rstrip())
    return ans
