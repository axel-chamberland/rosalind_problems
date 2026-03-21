"""
Author: Bulletic
Date: 2026-01-06
Rosalind problem ID: IPRB


Given: Three positive integers k, m, and n,
representing a population containing k+m+n organisms:
k individuals are homozygous dominant for a factor,
m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating
organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype).
Assume that any two organisms can mate.


"""

import sys


def main():
    # Get the number of individuals
    with open(sys.argv[1]) as f:
        n_dom, n_hetero, n_rec = f.read().strip().split()

    n_dom = int(n_dom)
    n_hetero = int(n_hetero)
    n_rec = int(n_rec)

    # Calculate the probability that
    # the children of two of these individuals
    # possess a dominant allele
    # Out of four cases in a Punett square, this represents
    # three of them (in the law of segregation, only when both
    # parents give a recessive gene does the children not have
    # the dominant allele

    # Calculate the amount of different alleles
    allele_dom = (n_dom) + (n_hetero)
    allele_rec = (n_hetero) + (n_rec)

    # The probability of a recessive child can be decomposed
    # into 3 possibilites:
    # Prob of two homozygote recessive parents * 100%
    # Prob of one homozygote parent and one heterozygote dom parent * 50%
    # prob of two hetero parents * 25%
    # You must use combinatories: the probability of the new parent having
    # the desired alleles depends on the alleles of the previous parent

    n_total = (n_dom) + (n_hetero) + (n_rec)

    P_homo_rec_parents = (n_rec / n_total) * ((n_rec - 1) / (n_total - 1))

    # There are two instances (one parent or the other can be hetero)
    P_hetero_dom_homo_rec_parents = (
        2 * 0.5 * ((n_hetero / n_total) * (n_rec / (n_total - 1)))
    )

    P_hetero_parents = 0.25 * (n_hetero / n_total) * ((n_hetero - 1) / (n_total - 1))

    # Probability of a child with dominant allele
    P_dom = 1 - (P_homo_rec_parents + P_hetero_dom_homo_rec_parents + P_hetero_parents)

    print(P_dom)


if __name__ == "__main__":
    main()
