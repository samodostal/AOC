import sys

EXAMPLE_DATA = """
""".strip()

North = (-1, 0)
East = (0, 1)
South = (1, 0)
West = (0, -1)

dirs = [North, East, South, West]


def quadratic_formula(x, a, b, c):
    x1 = a
    x2 = b - a
    x3 = c - b

    return x1 + x2 * x + (x * (x - 1) // 2) * (x3 - x2)


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    start_row, start_col = 0, 0

    for col, line in enumerate(lines):
        for row, char in enumerate(line):
            if char == "S":
                start_row, start_col = row, col

    steps = 64
    current_tiles = set()
    current_tiles.add((start_row, start_col))

    while steps:
        tiles = current_tiles.copy()
        current_tiles = set()

        for tile in tiles:
            row, col = tile
            for d_row, d_col in dirs:
                new_row, new_col = row + d_row, col + d_col

                if (
                    new_row < 0
                    or new_row >= len(lines)
                    or new_col < 0
                    or new_col >= len(lines[0])
                ):
                    continue

                if lines[new_row][new_col] == "#":
                    continue

                current_tiles.add((new_row, new_col))
        steps -= 1

    answer1 = len(current_tiles)

    # Part 2
    steps = 0
    current_tiles = set()
    current_tiles.add((start_row, start_col))
    len_rows, len_cols = len(lines), len(lines[0])

    mod_values = []
    mod_steps = [65, 65 + len_rows, 65 + len_rows * 2]

    while True:
        tiles = current_tiles.copy()
        current_tiles = set()

        if steps in mod_steps:
            mod_steps.remove(steps)
            mod_values.append(len(tiles))

        if not mod_steps:
            break

        for tile in tiles:
            row, col = tile
            for d_row, d_col in dirs:
                new_row, new_col = row + d_row, col + d_col

                mod_row, mod_col = new_row % len_rows, new_col % len_cols

                if lines[mod_row][mod_col] == "#":
                    continue

                current_tiles.add((new_row, new_col))
        steps += 1

    answer2 = quadratic_formula(26501365 // len(lines), *mod_values)

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
