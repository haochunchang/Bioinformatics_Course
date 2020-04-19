"""
Example solution to 04_data_structure.py
"""
from typing import List

def find_ori(dna: list, ori: str) -> int:
    """
    A circular DNA, find the origin of replication
    Given:
        dna: a list of nucleotides ATCG (e.g.: ['A', 'T', 'C', 'C', 'G'])
        ori: a string of nucleotides (e.g.: "CGA")
    Return:
        start index of dna where ori starts. (e.g.: 3)
        (any of them)
    """

    if len(ori) > len(dna):
        print("ori longer than dna, no need to find.")
        return -1

    circular_dna = dna
    for i in range(len(ori) - 1):
        circular_dna.append(dna[i])

    for i in range(len(circular_dna) - len(ori) + 1):
        frag = circular_dna[i:i + len(ori)]
        frag = ''.join(frag)
        if frag == ori:
            return i % len(dna)
    return -1

def is_on_the_sameline(points: List[tuple]) -> bool:
    """
    Assume both x and y > 0 and are integers.
    Given:
        points: [(x1, y1), (x2, y2), (x3, y3), ...] at least 3 points
    Return:
        True if all points are on the same line else False
    """
    dx = points[1][0] - points[0][0]
    dy = points[1][1] - points[0][1]
    vertical, horizontal = False, False
    if dx == 0:
        vertical = True
    elif dy == 0:
        horizontal = True
    else:
        slope = dy / dx

    test_dx, test_dy = 0, 0
    test_slope = 0.0

    for i in range(2, len(points)):
        test_dx = points[i][0] - points[0][0]
        test_dy = points[i][1] - points[0][1]
        if vertical:
            if test_dx != 0:
                return False
        elif horizontal:
            if test_dy != 0:
                return False
        else:
            test_slope = test_dy / test_dx
            if test_slope != slope:
                return False
    return True


def count_unique_genes(gene_list1: List[str],
                       gene_list2: List[str]) -> int:
    """
    Given:
        gene_list: list of string
    Return:
        number of unique genes appear in both list.
    """
    intersect = set(gene_list1).intersection(set(gene_list2))
    return len(intersect)


def count_amino_acids(protein: str) -> dict:
    """
    Given:
        protein: a string of protein sequence
    Return:
        A dictionary contains: {amino acid: number of occurrence in protein}
    (If some amino acids do not appear in protein,
     the output does not need to include it.)
    """
    count = {}
    for a in protein:
        if a not in count:
            count[a] = 1
        else:
            count[a] += 1
    return count
