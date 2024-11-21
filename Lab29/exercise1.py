# 1. a. Given a set of motifs {AATGG, TAACA, TCGCC, AGGCC,
# AGTCC, CGACC}, provide a regular expression for obtaining the
# motifs that begin with T.

import re

def motif_match():

    motif = {'AATGG', 'TAACA', 'TCGCC', 'AGGCC', 'AGTCC', 'CGACC'}
    pattern = re.compile("^T")
    result = [m for m in motif if pattern.search(m)]
    print(result)

def main():
    motif_match()


if __name__ == '__main__':
    main()