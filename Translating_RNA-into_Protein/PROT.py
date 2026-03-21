import sys

from Bio.Seq import Seq

"""
Author: Bulletic
Date: 2026-01-07
Rosalind problem ID: PROT

Given: An RNA string s corresponding to
a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s
"""

# While I could make a dictionary with all codons, I don't have
# the time to do this. I will use biopython.

def main():
    # Get the number of individuals
    with open(sys.argv[1]) as f:
        dna_seq = f.read().strip()

    # Create a Seq object
    dna_seq = Seq(dna_seq)

    # Translate the object
    prot_seq = dna_seq.translate(stop_symbol="")
    print(prot_seq)


if __name__ == "__main__":
    main()
