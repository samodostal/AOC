import sys
from collections import defaultdict

EXAMPLE_DATA = """
""".strip()

# [dx, dy]
DIRS_DIAGS = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
DIAGS = [[1, 1], [1, -1], [-1, -1], [-1, 1]]


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    grid = list(filter(None, data.split("\n")))

    D = defaultdict(lambda: ".")
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            D[(x, y)] = grid[x][y]

    # Part 1
    for x, y in list(D.keys()):
        if D[(x, y)] != "X":
            continue

        for [dx, dy] in DIRS_DIAGS:
            valid_dir = True
            for i, char in enumerate("MAS"):
                if D[(x + (dx * (i + 1)), y + (dy * (i + 1)))] != char:
                    valid_dir = False
                    break

            if valid_dir:
                answer1 += 1

    # Part 2
    for x, y in list(D.keys()):
        if D[(x, y)] != "A":
            continue

        chars = []
        for [dx, dy] in DIAGS:
            chars.append(D[x + dx, y + dy])

        if (
            chars.count("M") == 2
            and chars.count("S") == 2
            and (chars[0] == chars[1] or chars[1] == chars[2])
        ):
            answer2 += 1

    print(answer1, answer2)


if __name__ == "__main__":
    main()
