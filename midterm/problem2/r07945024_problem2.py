"""
Problem 2
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
            codons[codon] = aa_code
    return codons


def translate(rna):
    """
    Translate RNA sequence into Protein sequence
    Starting from the first nucleotides
    """
    codons = read_codons(join(MODULE_DIR, "codon.txt"))
    protein = ""
    for i in range(0, len(rna), 3):
        base = rna[i : i + 3]
        if len(base) != 3 or codons[base] == "Stop":
            break
        protein += codons[base]
    return protein


if __name__ == "__main__":
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
            f.write(your_ans + "\n")
