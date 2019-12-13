import numpy as np
from itertools import product

GAP_CHAR = '_'

def global_alignment(dataset: str, match_score=1, gap_score=-1, mismatch_score=-1) -> list:
    """
    Needleman–Wunsch algorithm for dataset: "stringA"\n"stringB"\n

    Assume scoring matrix is:
        match = 1, mismatch = -1, gap("_") = -1

    Returns a optimal alignment and its matching score.
    """
    a, b = dataset.splitlines()
    nrow = len(b) + 1
    ncol = len(a) + 1
    # construct matrix
    scoring = [[0 for i in range(ncol)] for i in range(nrow)]
    scoring = np.array(scoring)

    scoring[:,0] = [mismatch_score*i for i in range(nrow)]
    scoring[0,:] = [mismatch_score*i for i in range(ncol)]
    
    path = [  [list('u')] + [list() for i in range(ncol-1)] for i in range(nrow) ]
    path[0][1:] = [list('l') for i in range(ncol-1)]
    path[0][0] = ['']
   
    # Start fill in score
    for i in range(1, nrow):
        for j in range(1, ncol):

            pre = {}
            if a[j-1] == b[i-1]:
                cur = match_score
            else:
                cur = mismatch_score

            pre['l'] = scoring[i, j-1] + gap_score 
            pre['u'] = scoring[i-1, j] + gap_score
            pre['d'] = scoring[i-1, j-1] + cur

            scoring[i, j] = max(pre.values())
            sources = [k for k, v in pre.items() if v == scoring[i,j]]

            for s in sources:
                path[i][j].append(s)
    
    # Traceback multiple paths: construct graph, DFS
    cur_row = len(b)
    cur_col = len(a)
    path1, path2 = "", ""
   
    score = 0
    while cur_row > 0 and cur_col > 0:
        
        direction = path[cur_row][cur_col]
        d = direction[0]
        
        #print("row: {}, col: {}, d: {}".format(cur_row, cur_col, d))
        if d == 'd':
            cur_row -= 1
            cur_col -= 1
            path1 = a[cur_col] + path1
            path2 = b[cur_row] + path2
            if path1[0] == path2[0]: score += match_score
            else: score += mismatch_score 
        elif d == 'u': 
            cur_row -= 1
            path1 = GAP_CHAR + path1
            path2 = b[cur_row] + path2
            score += gap_score
        elif d == 'l':
            cur_col -= 1
            path1 = a[cur_col] + path1
            path2 = GAP_CHAR + path2
            score += gap_score
        else:
            continue
        #print(path1, path2)
    return "{}\n{}".format(path1, path2), score


def calculate_score(dataset: str, match_score=1, gap_score=-1, mismatch_score=-1) -> int:

    a, b = dataset.splitlines()
    score = 0
    for s1, s2 in zip(a, b):
        if s1 == GAP_CHAR or s2 == GAP_CHAR:
            score += gap_score
        elif s1 == s2:
            score += match_score
        else:
            score += mismatch_score

    return score

if __name__ == "__main__":
    #data = 'ATCGA\nATCG\n'
    data = "GCATGCU\nGATTACA\n"
    result, score = global_alignment(data)
    print(result, score)
