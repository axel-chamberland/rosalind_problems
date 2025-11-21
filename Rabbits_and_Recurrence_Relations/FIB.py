import sys

with open(sys.argv[1]) as f:
    months, multiplier = f.read().split(sep=" ")
    multiplier = int(multiplier)
    months = int(months)

    pairs_list = [1, 1]

    for month in range(months):
        n = pairs_list[month] + pairs_list[month-1]*multiplier # NOTE: WRONG
        pairs_list.append(n)

    print(pairs_list[-1])
    print(pairs_list)