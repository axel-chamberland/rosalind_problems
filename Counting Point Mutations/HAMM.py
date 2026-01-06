"""
Author: Bulletic
Date: 2026-01-05
Rosalind problem ID: HAMM

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t)

"""

import sys

def main():
    with open(sys.argv[1]) as f:
        seqs = f.read().strip().upper().split()


    # My code does this, which works but is pretty ugly:
    distance = 0
    for i in range(max(len(seqs[0]), len(seqs[1]))):

        if len(seqs[0]) <= i or len(seqs[1]) <= i:
            distance += 1
            continue
        
        if seqs[0][i] != seqs[1][i]:
            distance += 1

    # I could have used this instead, but
    # I did not know how to use zip:

    # distance = abs(len(seqs[0]) - len(seqs[1]))

    # distance += sum(x != y for x, y in zip(seqs[0], seqs[1]))

    print(distance)

if __name__ == "__main__":
    main()
