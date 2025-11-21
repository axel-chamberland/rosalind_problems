import sys
with open(sys.argv[1]) as s:
    dna_seq = s.read().strip().upper()

    dict = {"A":"T", "T":"A", "G":"C", "C":"G"}
    rna_seq = ""
    for c in dna_seq[::-1]:
        rna_seq += dict[c]
        

    print(rna_seq)