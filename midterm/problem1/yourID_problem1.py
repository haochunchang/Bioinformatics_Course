"""
Problem 1
"""


def find_ori(dna, ori):
    """
    Identify start and end index of the origin of replication
    in the given circular DNA.
    """
    pass
    # circular_dna = [x for x in dna]
    # start, end = -1, -1

    # convert dna into circular dna

    # for i in range():
    #    fragment = circular_dna[i:i + len(ori)]
    #    fragment = ''.join(frag)
    #    if fragment == ori:
    #
    # return start, end


if __name__ == "__main__":
    # Do not modify this part!!!
    # If you change the output format, you may lose you private testing score
    # Since TA use this format to grade the answers
    import sys

    input_path, output_path = sys.argv[1], sys.argv[2]

    test_dnas = []
    test_ans = []
    with open(input_path, "r") as f, open(output_path, "w") as o:
        for i, line in enumerate(f):
            inputs, ans = line.split("\t")
            dna, ori = inputs.split(",")
            start, end = ans.split(",")

            your_start, your_end = find_ori(dna, ori)
            your_ans = "{},{}".format(your_start, your_end)
            # Uncomment the following line if you want to check your answers one by one.
            # assert your_ans == ans, "Wrong answer at input#{}".format(i+1)
            o.write(your_ans + "\n")
