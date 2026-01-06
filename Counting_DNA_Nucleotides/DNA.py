"""
Author: Bulletic
Date: 2025/11/02
Rosalind problem ID: DNA
"""

import sys
from collections import Counter

def main():
    
    # Pipe the DNA sequence as a string
    with open(sys.argv[1], "r") as s:
        seq = s.read().strip().upper()

        counts = Counter(seq)
        count_a = counts.get("A", 0)
        count_c = counts.get("C", 0)
        count_g = counts.get("G", 0)
        count_t = counts.get("T", 0)

        print(count_a, count_c, count_g, count_t)

if __name__ == "__main__":
    main()


