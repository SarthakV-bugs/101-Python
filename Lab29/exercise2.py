# 2. Generate a random DNA sequence with the four bases. Write a
# function that checks if the sequence contains only valid DNA bases
# # (A, T, C, G) using a regular expression.

import re
import random

def valid_bases(dna):
    pattern = re.compile("^[ATGC]+$")
    if pattern.match(dna):
        print("DNA sequence contains valid bases.")
    else:
        print("Invalid bases in the DNA sequences")

def main():
    dna = ''
    bases = ['A','G','T','C']
    n = int(input("Enter the length of seq: "))
    dna += ''.join(random.choice(bases) for _ in range(n))
    print(dna)
    valid_bases(dna)



if __name__ == '__main__':
    main()