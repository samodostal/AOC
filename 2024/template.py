import sys
import math
import re
from collections import defaultdict

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
    G = defaultdict(lambda: "O", {(x, y,): lines[ y ][x] for x in range(len(lines[0])) for y in range(len(lines))})

    # cc

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
