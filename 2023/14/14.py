import sys

EXAMPLE_DATA = """

O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....

""".strip()


def tilt_map(map, dir):
    lines = list(filter(None, map.split("\n")))
    rocks = []

    if dir == [-1, 0] or dir == [0, -1]: # North West
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == "O":
                    rocks.append((row, col))
    elif dir == [1, 0]: # South
        for row, line in enumerate(reversed(lines)):
            for col, char in enumerate(line):
                if char == "O":
                    rocks.append((len(lines) - row - 1, col))
    else: # East
        for row, line in enumerate(lines):
            for col, char in enumerate(reversed(line)):
                if char == "O":
                    rocks.append((row, len(line) - col - 1))

    for rock in rocks:
        row, col = rock
        oldrow, oldcol = row, col

        while True:
            new_row, new_col = row + dir[0], col + dir[1]
            if (
                new_row < 0
                or new_row >= len(lines)
                or new_col < 0
                or new_col >= len(lines[0])
            ):
                break

            if lines[new_row][new_col] == ".":
                row, col = new_row, new_col
                continue

            if lines[new_row][new_col] == "#" or lines[new_row][new_col] == "O":
                break

        oldline = lines[oldrow]
        oldline = oldline[:oldcol] + "." + oldline[oldcol + 1 :]
        lines[oldrow] = oldline

        line = lines[row]
        line = line[:col] + "O" + line[col + 1 :]
        lines[row] = line

    return "\n".join(lines)


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    chunks = list(filter(None, data.split("\n\n")))

    new_map = tilt_map(chunks[0], [-1, 0])

    lines = list(filter(None, new_map.split("\n")))
    for row, line in enumerate(lines):
        for _, char in enumerate(line):
            if char == "O":
                answer1 += len(lines) - row

    # Part 2
    cycle_100_map = None
    cycled_map = chunks[0]

    cycle = 0

    while True:
        cycle += 1
        for dir in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            cycled_map = tilt_map(cycled_map, dir)

        if cycle == 100:
            cycle_100_map = cycled_map
            continue

        if cycle_100_map == cycled_map:
            break

    period = cycle - 100
    to_finish_cycles = (1000000000 - 100) % period

    while to_finish_cycles:
        to_finish_cycles -= 1
        for dir in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            cycled_map = tilt_map(cycled_map, dir)

    lines = list(filter(None, cycled_map.split("\n")))
    for row, line in enumerate(lines):
        for _, char in enumerate(line):
            if char == "O":
                answer2 += len(lines) - row

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
