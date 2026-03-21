import sys

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction



def main():

    records = {}
    for record in SeqIO.parse(sys.argv[1], "fasta"):
        records[record.id] = gc_fraction(record.seq) * 100

    sorted_records = sorted(records.items(), key=lambda x:x[1], reverse=True) # Credit: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
    print(sorted_records[0][0], sorted_records[0][1], sep="\n")

if __name__ == "__main__":
    main()
