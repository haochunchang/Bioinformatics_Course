"""
Functions for loading testing data
"""

GAP_CHAR = "_"


def load_data(filepath):

    test_ans = []
    with open(filepath, "r") as f:
        for line in f:
            sequences, score = line.split("\t")
            seq1, seq2 = sequences.split(",")
            check_seq_score = int(score.rstrip())
            test_ans.append((check_seq_score, int(score.rstrip())))
    return test_ans


def load_answer(filepath):

    ans = []
    with open(filepath, "r") as f:
        for line in f:
            seqs, score = line.split("\t")
            seq1, seq2 = seqs.split(",")
            check_seq_score = calculate_score(seq1, seq2)
            ans.append((check_seq_score, int(score.rstrip())))
    return ans


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
