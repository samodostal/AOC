import sys
import re

EXAMPLE_DATA = """
""".strip()


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))
    numbers_per_line = [[int(n) for n in re.findall(r"-?\d+", line)] for line in lines]

    # Part 1
    low = []
    high = []

    for [l, h] in numbers_per_line:
        low.append(l)
        high.append(h)

    low.sort()
    high.sort()

    for i in range(len(low)):
        answer1 += abs(high[i] - low[i])

    # Part 2
    dict = {}

    for [_, h] in numbers_per_line:
        if dict.get(h) == None:
            dict[h] = 0
        dict[h] += 1

    for l in low:
        h = dict.get(l, 0)
        answer2 += l * h

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
