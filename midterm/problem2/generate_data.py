import sys
import random
from r07945024_problem2 import translate

num_case = int(sys.argv[1])
bases = ["A", "U", "C", "G"]

with open(sys.argv[2], "w") as f:
    for i in range(num_case):
        rnalength = random.randint(20, 1000)
        rna = "".join(random.choices(bases, k=rnalength))
        protein = translate(rna)
        f.write(rna + "," + protein + "\n")
