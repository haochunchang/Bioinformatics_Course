"""
Generate testing data for problem1
"""
import sys
import random
from r07945024_problem3 import pairwise_alignment, calculate_score

num_case = int(sys.argv[1])
bases = ["A", "T", "C", "G"]

with open(sys.argv[2], "w") as f:
    for _ in range(num_case):

        # length = random.randint(5, 100)
        length = random.randint(100, 1000)
        seq1 = "".join(random.choices(bases, k=length))
        seq2 = "".join(random.choices(bases, k=length))
        aligned, score = pairwise_alignment(seq1, seq2)

        f.write(seq1 + "," + seq2 + "\t")
        f.write(str(score) + "\n")
