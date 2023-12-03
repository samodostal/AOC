import sys
import re

EXAMPLE_DATA = """
""".strip()

# gears = { "125:38": [253478, False] }
gears = {}


def is_adjacent(col, row, num, map):
    num_length = len(str(num))

    for c in range(col - 1, col + num_length + 1):
        for r in range(row - 1, row + 2):
            if r < 0 or r >= len(map):
                continue
            if c < 0 or c >= len(map[row]):
                continue

            if not map[r][c].isdecimal() and map[r][c] != ".":
                return True

    return False


def find_gears(col, row, num, map):
    num_length = len(str(num))

    for c in range(col - 1, col + num_length + 1):
        for r in range(row - 1, row + 2):
            if r < 0 or r >= len(map):
                continue
            if c < 0 or c >= len(map[row]):
                continue

            if map[r][c] == "*":
                if gears.get(str(r) + ":" + str(c)) == None:
                    gears[str(r) + ":" + str(c)] = [num, False]
                else:
                    prev_num = gears[str(r) + ":" + str(c)][0]
                    gears[str(r) + ":" + str(c)] = [num * prev_num, True]


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    p = re.compile("[0-9]+")
    row = 0

    for line in lines:
        for num in p.finditer(line):
            if is_adjacent(num.start(), row, int(num.group()), lines):
                answer1 += int(num.group())

            find_gears(num.start(), row, int(num.group()), lines)
        row += 1

    for [num, is_complete] in gears.values():
        if is_complete:
            answer2 += num

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
