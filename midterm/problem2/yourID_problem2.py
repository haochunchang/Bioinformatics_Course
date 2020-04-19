"""
Problem 2: Translating RNA into Protein (30%)
Description:
    Write a function that can translate RNA sequence into protein sequence.
    Start from the first nucleotide. (Ignore start codon)
    Stop translating when you encounter “Stop codon”.

Input:
    rna: string, RNA sequence (e.g. AUGUAA)

Output:
    A string of protein sequences translated from input
    (e.g. M) Explanation: AUG -> M, UAA -> Stop
"""
from os.path import join, dirname, realpath

MODULE_DIR = dirname(realpath(__file__))


def read_codons(path):
    """
    Returns: {"RNA": Amino Acid}
    """
    codons = {}
    with open(path, "r") as f:
        for line in f:
            codon, aa_code = line.split()
            # Put amino acid code into dictionary
    return codons


def translate(rna):
    """
    Translate RNA sequence into Protein sequence
    Starting from the first nucleotides
    """
    pass
    # codons = read_codons(join(MODULE_DIR, "codon.txt"))
    # protein = ""
    # for i in range():
    #    base =
    #    if len(base) != 3 or codons[base] == :
    #        break
    #    protein +=
    # return protein


if __name__ == "__main__":
    # Do not modify this part!!!
    # If you change the output format, you may lose you private testing score
    # Since TA use this format to grade the answers
    import sys

    input_path, output_path = sys.argv[1], sys.argv[2]

    test_rnas = []
    test_ans = []
    with open(input_path, "r") as f:
        for line in f:
            rna, ans = line.split(",")
            test_rnas.append(rna)
            test_ans.append(ans)

    with open(output_path, "w") as f:
        for i, (rna, ans) in enumerate(zip(test_rnas, test_ans)):
            your_ans = translate(rna)
            # Uncomment the following line if you want to check your answers.
            # assert (your_ans + "\n") == ans, "Wrong answer at input#{}".format(i+1)
            f.write(your_ans + "\n")
