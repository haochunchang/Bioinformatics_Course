"""
Problem 1
"""


def find_ori(dna, ori):
    """
    Identify start and end index of the origin of replication
    in the given circular DNA.
    """
    circular_dna = [x for x in dna]
    start, end = -1, -1

    for i in range(len(ori) - 1):
        circular_dna.append(dna[i])

    for i in range(len(circular_dna) - len(ori) + 1):
        frag = circular_dna[i : i + len(ori)]
        frag = "".join(frag)
        if frag == ori:
            start = i % len(dna)
            end = (start + len(ori)) % len(dna)
            break
    return start, end


if __name__ == "__main__":
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
            # Uncomment the following line if you want to check your answers.
            # assert your_ans == ans, "Wrong answer at input#{}".format(i+1)
            o.write(your_ans + "\n")
