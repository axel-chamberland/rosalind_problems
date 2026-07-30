import sys


def main():

    with open(sys.argv[1]) as f:
        months, max_age = f.read().split(sep=" ")
        months = int(months)
        max_age = int(max_age)

        # start with 2 rabbits at age = 0 months
        monthly_pairs = [1]

        for month in range(1, months):
            newborns = 0

            # mature_pairs : alive_pairs - last gen = from month-max_age to before last gen
            start = month - max_age
            if start < 1:
                start = 0

            for pairs in monthly_pairs[start:-1]:
                # All mature rabits reproduce with a multiplier of 1 (implicit)
                newborns += pairs

            monthly_pairs.append(newborns)

        start = months - max_age
        if start < 0:
            start = 0
        alive_pairs = sum(monthly_pairs[start:])
        print(alive_pairs)


if __name__ == "__main__":
    main()
