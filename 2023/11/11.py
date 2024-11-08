import sys

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

    empty_rows = []
    empty_cols = []
    galaxies = []

    for row, line in enumerate(lines):
        is_empty_row = True
        for char in line:
            if char != ".":
                is_empty_row = False
                break

        if is_empty_row:
            empty_rows.append(row)

    for col in range(len(lines[0])):
        is_empty_col = True
        for line in lines:
            if line[col] != ".":
                is_empty_col = False
                break

        if is_empty_col:
            empty_cols.append(col)

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "#":
                galaxies.append((row, col))

    checked_combinations = set()

    for g1 in galaxies:
        for g2 in galaxies:
            if (g2, g1) in checked_combinations:
                continue

            (row1, col1) = g1
            (row2, col2) = g2
            empty_rows_between = 0
            empty_cols_between = 0

            for empty_row in empty_rows:
                if (empty_row > row1 and empty_row < row2) or (
                    empty_row < row1 and empty_row > row2
                ):
                    empty_rows_between += 1

            for empty_col in empty_cols:
                if (empty_col > col1 and empty_col < col2) or (
                    empty_col < col1 and empty_col > col2
                ):
                    empty_cols_between += 1

            distance_row = (
                abs(row1 - row2) - empty_rows_between + (empty_rows_between * 1000000)
            )
            distance_col = (
                abs(col1 - col2) - empty_cols_between + (empty_cols_between * 1000000)
            )

            answer1 += distance_row + distance_col

            checked_combinations.add((g1, g2))

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
