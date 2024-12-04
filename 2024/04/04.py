import sys

EXAMPLE_DATA = """
""".strip()


def get_rows_cols_diags_as_strings(rows, max_row, max_col):
    cols = [
        "".join([rows[row][col] for row in range(max_row)]) for col in range(max_col)
    ]

    diags_lr = [
        "".join([rows[row + i][i] for i in range(min(max_row - row, max_col))])
        for row in range(max_row)
    ]
    diags_lr += [
        "".join([rows[i][col + i] for i in range(min(max_row, max_col - col))])
        for col in range(1, max_col)
    ]

    diags_rl = [
        "".join(
            [rows[row + i][max_col - 1 - i] for i in range(min(max_row - row, max_col))]
        )
        for row in range(max_row)
    ]
    diags_rl += [
        "".join(
            [rows[i][max_col - 1 - col - i] for i in range(min(max_row, max_col - col))]
        )
        for col in range(1, max_col)
    ]

    return rows, cols, diags_lr, diags_rl


def check_for_structure(rows, row, col):
    chars = []
    for [r, c] in [[row - 1, col - 1], [row + 1, col - 1]]:
        if r >= 0 and c >= 0 and r < len(rows) and c < len(rows):
            chars.append(rows[r][c])

    for [r, c] in [[row + 1, col + 1], [row - 1, col + 1]]:
        if r >= 0 and c >= 0 and r < len(rows) and c < len(rows):
            chars.append(rows[r][c])

    return (
        chars.count("S") == 2
        and chars.count("M") == 2
        and (chars[0] == chars[1] or chars[1] == chars[2])
    )


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    rows = list(filter(None, data.split("\n")))

    # Part 1
    (rows, cols, diags_lr, diags_rl) = get_rows_cols_diags_as_strings(
        rows, len(rows), len(rows)
    )

    answer1 += sum([s.count("XMAS") + s.count("SAMX") for s in rows])
    answer1 += sum([s.count("XMAS") + s.count("SAMX") for s in cols])
    answer1 += sum([s.count("XMAS") + s.count("SAMX") for s in diags_lr])
    answer1 += sum([s.count("XMAS") + s.count("SAMX") for s in diags_rl])

    # Part 2
    for row in range(len(rows)):
        for col in range(len(cols)):
            char = rows[row][col]
            if char == "A":
                if check_for_structure(rows, row, col):
                    answer2 += 1

    print(answer1, answer2)


if __name__ == "__main__":
    main()
