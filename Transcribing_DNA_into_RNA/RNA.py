"""
Author: djxel
Date: 2025/11/02
Rosalind problem ID: RNA
"""

import sys

def main():
    
    # Pipe the DNA sequence as a string
    with open(sys.argv[1], "r") as s:
        dna_seq = s.read().strip().upper()

        rna_seq = ""
        for c in dna_seq:
            if c == "T":
                rna_seq += "U"
            else:
                rna_seq += c

        print(rna_seq)

if __name__ == "__main__":
    main()


