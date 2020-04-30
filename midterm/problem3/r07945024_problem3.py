import numpy as np
from typing import Tuple

GAP_CHAR = "_"


def pairwise_alignment(seq1: str, seq2: str) -> Tuple[str, int]:
    """
    Needleman–Wunsch algorithm for 2 strings
    Returns:
        (an optimal alignment, its matching score)
    """
    nrow = len(seq2) + 1
    ncol = len(seq1) + 1

    match_score = 1
    mismatch_score = -1
    gap_score = -1

    # construct matrix
    scoring = [[0 for i in range(ncol)] for i in range(nrow)]
    scoring = np.array(scoring)
    scoring[:, 0] = [mismatch_score * i for i in range(nrow)]
    scoring[0, :] = [mismatch_score * i for i in range(ncol)]

    path = [[list("u")] + [list() for i in range(ncol - 1)] for i in range(nrow)]
    path[0][1:] = [list("l") for i in range(ncol - 1)]
    path[0][0] = [""]

    # Start fill in score
    for i in range(1, nrow):
        for j in range(1, ncol):

            pre = {}
            if seq1[j - 1] == seq2[i - 1]:
                cur = match_score
            else:
                cur = mismatch_score

            pre["l"] = scoring[i, j - 1] + gap_score
            pre["u"] = scoring[i - 1, j] + gap_score
            pre["d"] = scoring[i - 1, j - 1] + cur

            scoring[i, j] = max(pre.values())
            sources = [k for k, v in pre.items() if v == scoring[i, j]]

            for s in sources:
                path[i][j].append(s)

    # Traceback paths
    cur_row = len(seq2)
    cur_col = len(seq1)
    path1, path2 = "", ""

    score = 0
    while cur_row > 0 or cur_col > 0:

        direction = path[cur_row][cur_col]

        # select one source arbitrarily
        d = direction[0]

        # print("row: {}, col: {}, d: {}".format(cur_row, cur_col, d))
        if d == "d":
            cur_row -= 1
            cur_col -= 1
            path1 = seq1[cur_col] + path1
            path2 = seq2[cur_row] + path2
            if path1[0] == path2[0]:
                score += match_score
            else:
                score += mismatch_score
        elif d == "u":
            cur_row -= 1
            path1 = GAP_CHAR + path1
            path2 = seq2[cur_row] + path2
            score += gap_score
        elif d == "l":
            cur_col -= 1
            path1 = seq1[cur_col] + path1
            path2 = GAP_CHAR + path2
            score += gap_score

    return "{},{}".format(path1, path2), score


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
            # assert your_score == int(ans), "{}/{} Wrong answer at input#{}".format(your_score, score, i+1)
            o.write("{},{}\t{}\n".format(seq1, seq2, your_score))
