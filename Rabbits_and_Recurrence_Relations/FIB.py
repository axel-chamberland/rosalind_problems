import sys

with open(sys.argv[1]) as f:
    months, multiplier = f.read().split(sep=" ")
    multiplier = int(multiplier)
    months = int(months)

    pairs_list = [1, 1]

    for month in range(2, months):
        print(month)
        print(pairs_list[month-1])
        n = pairs_list[month-1] + pairs_list[month-2]*multiplier
        pairs_list.append(n)

    print(pairs_list[-1])
    print(pairs_list)
