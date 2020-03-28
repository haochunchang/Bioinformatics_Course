"""
Generate testing data for problem1
"""
import sys
import random
from r07945024_problem1 import find_ori

num_case = int(sys.argv[1])
bases = ["A", "T", "C", "G"]

with open(sys.argv[2], "w") as f:
    for i in range(num_case):
        have_ori = random.choices([0, 1], weights=[0.25, 0.75])

        # length = random.randint(16000, 1e5)
        length = random.randint(160, 1000)
        dna = "".join(random.choices(bases, k=length))

        if have_ori:
            ori_len = random.randint(3, 10)
            ori_index = random.randint(0, len(dna))
            ori = dna[ori_index : ori_index + ori_len]
            start, end = find_ori(dna, ori)
        else:
            ori = "".join(random.choices(bases, k=random.randint(3, 10)))
            start, end = find_ori(dna, ori)
        f.write(dna + "," + ori + "\t")
        f.write(str(start) + "," + str(end) + "\n")
