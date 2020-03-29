"""
Functions for loading testing data
"""


def load_data(filepath):
    test_ans = []
    with open(filepath, "r") as f:
        for line in f:
            name, ans = line.split("\t")
            test_ans.append(ans)
    return test_ans


def load_answer(filepath):
    ans = []
    with open(filepath, "r") as f:
        for line in f:
            ans.append(line)
    return ans
