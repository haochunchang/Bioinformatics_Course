"""
For 03_process.py
"""
def validate_base(base, rnaflag=False):
    """
    check base only have ACGT or ACGU
    """
    validate = "ACGTacgt"
    if rnaflag:
        validate = validate.replace("T", "U")
        validate = validate.replace("t", "u")

    if len(set(base) - set(validate)) != 0:
        return False
    return True


def transcribe(dna: str) -> str:
    """
    Convert T in dna to U
    """
    dna = dna.upper()
    if not validate_base(dna):
        return "It is not a DNA string!!"

    rna = ""
    for nucleotide in dna:
        if nucleotide == "T":
            rna += "U"
        else:
            rna += nucleotide
    return rna


def count_nucleotides(dna: str) -> str:
    """
    Return count of A C G T in a string
    """
    count = {"A" : 0,
             "C" : 0,
             "G" : 0,
             "T" : 0}
    dna = dna.upper()
    if not validate_base(dna):
        return "It is not a DNA string!!"

    for nucleotide in dna:
        count[nucleotide] += 1

    return "{} {} {} {}".format(count["A"], count["C"], count["G"], count["T"])
