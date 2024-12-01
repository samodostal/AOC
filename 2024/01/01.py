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
    chunks = list(filter(None, data.split("\n\n")))
    lines = list(filter(None, data.split("\n")))
    numbers_per_line = [[int(n) for n in re.findall(r"-?\d+", line)] for line in lines]
    splits_per_line = [line.split() for line in lines]

    # Part 1
    low = []
    high = []

    for numbers in numbers_per_line:
        [l, h] = numbers
        low.append(l)
        high.append(h)

    low.sort()
    high.sort()

    for i in range(len(low)):
        answer1 += abs(high[i] - low[i])

    # Part 2
    dict = {}

    for numbers in numbers_per_line:
        [_, h] = numbers

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
