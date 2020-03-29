from collections import OrderedDict
from typing import Tuple

GAP_CHAR = "_"


def pairwise_alignment(seq1: str, seq2: str) -> Tuple[str, int]:
    """
    Needleman–Wunsch algorithm for 2 strings
    Returns:
        (an optimal alignment, its matching score)
    """
    pass
    # nrow =
    # ncol =

    # match_score = 1
    # mismatch_score = -1
    # gap_score = -1

    # construct matrix
    # scoring =

    # scoring[:, 0] = [mismatch_score * i for i in range(nrow)]

    # path =

    # Start fill in score
    # for i in range(1, nrow):
    #    for j in range(1, ncol):

    #        if seq1[j - 1] == seq2[i - 1]:
    #        else:

    #        pre = OrderedDict()
    #        pre['l'] =
    #        pre['u'] =
    #        pre['d'] =

    #        scoring[i, j] = max()

    #        Record score source in path

    # Traceback paths
    # cur_row =
    # cur_col =
    # path1, path2 = "", ""

    # score = 0
    # while cur_row > 0 and cur_col > 0:

    #     direction = path[cur_row][cur_col]

    #     print("row: {}, col: {}, d: {}".format(cur_row, cur_col, d))
    #    if d == 'd':
    #        pass
    #    elif d == 'u':
    #        pass
    #    elif d == 'l':
    #        pass
    # return "{},{}".format(path1, path2), score


def calculate_score(seq1, seq2, match_score=1, gap_score=-1, mismatch_score=-1) -> int:

    score = 0
    for s1, s2 in zip(seq1, seq2):
        if s1 == GAP_CHAR or s2 == GAP_CHAR:
            score += gap_score
        elif s1 == s2:
            score += match_score
        else:
            score += mismatch_score
    return score


if __name__ == "__main__":
    # Do not modify this part!!!
    # If you change the output format, you may lose you private testing score
    # Since TA use this format to grade the answers
    import sys

    input_path, output_path = sys.argv[1], sys.argv[2]

    with open(input_path, "r") as f, open(output_path, "w") as o:
        for i, line in enumerate(f):
            inputs, ans = line.split("\t")
            seq1, seq2 = inputs.split(",")
            score = int(ans.rstrip())

            aligned, your_score = pairwise_alignment(seq1, seq2)
            your_ans = "{}\t{}".format(aligned, your_score)
            # Uncomment the following line if you want to check your answers one by one.
            # assert your_ans == ans, "Wrong answer at input#{}".format(i+1)
            o.write(your_ans + "\n")
