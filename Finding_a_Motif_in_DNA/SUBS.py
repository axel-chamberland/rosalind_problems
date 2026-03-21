import sys

from Bio.Seq import Seq

"""
Author: Bulletic
Date: 2026-01-07
Rosalind problem ID: SUBS

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

# I see a few ways to go at this:
# Iterating over all elements or using a partial index or a suffix table
# The simplets is the first method, while it is slower
# over huge data. We usually use spaced seeds to make faster approximatinos

def main():
    with open(sys.argv[1]) as f:
        s, t = f.read().strip().split()

    for i in range(len(s)):
        if i > len(s) - len(t):
            break

        if s[i:len(t)+i] == t:
            print(i+1, end=" ") # adjust by one for 1-based numbering



if __name__ == "__main__":
    main()
