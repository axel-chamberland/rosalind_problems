import sys
from typing import Counter

"""
Author: Bulletic
Date: 2026-01-07
Rosalind problem ID: CONS

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection.
(If several possible consensus strings exist, then you may return any one of them.)
"""


def main():
    with open(sys.argv[1]) as f:
        sequences = {}

        data = []
        seq = []
        for i, line in enumerate(f):
            if line.startswith(">"):
                if i == 0:
                    continue
                data.append("".join(seq))
                seq = []
                continue

            seq.append(line.strip().upper())

    data.append("".join(seq))
    n_rows, n_cols = len(data), len(data[0])

    profile_tbl = []

    result = []

    # Get profile table and consensus
    for i in range(n_cols):
        column = ""
        for j in range(n_rows):
            column += data[j][i]

        c = Counter(column)

        counts = []
        max_count = -1

        for nuc in ("A", "C", "G", "T"):
            count = c[nuc]
            if count > max_count:
                max_count = count
                maximum_nuc = nuc

            counts.append(count)

        result.append(maximum_nuc)

        profile_tbl.append(counts)

    # Print results
    print("".join(result))

    for i, nuc in enumerate(("A", "C", "G", "T")):
        print(
            f"{nuc}: {' '.join(str(profile_tbl[row][i]) for row in range(len(profile_tbl)))}"
        )

if __name__ == "__main__":
    main()
