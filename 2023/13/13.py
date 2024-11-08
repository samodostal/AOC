import sys

EXAMPLE_DATA = """
""".strip()


def count_smudges(start, end):
    smudges = 0
    for x in range(len(start)):
        for y in range(len(start[0])):
            if start[x][y] != end[x][y]:
                smudges += 1
    return smudges


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    chunks = list(filter(None, data.split("\n\n")))

    column_splits, row_splits = [], []

    for chunk in chunks:
        lines = list(filter(None, chunk.split("\n")))

        for col in range(1, len(lines[0])):
            are_same = True
            for line in lines:
                start, end = line[:col], line[col:]

                if len(start) < len(end):
                    end = end[: len(start)]
                    end = end[::-1]
                else:
                    start = start[::-1]
                    start = start[: len(end)]

                if start != end:
                    are_same = False

            if are_same:
                column_splits.append(col)
                break

        for row in range(1, len(lines)):
            start, end = lines[:row], lines[row:]

            if len(start) < len(end):
                end = end[: len(start)]
                end = end[::-1]
            else:
                start = start[::-1]
                start = start[: len(end)]

            if start == end:
                row_splits.append(row)
                break

    answer1 += sum(column_splits)
    answer1 += sum(row_splits) * 100

    column_splits, row_splits = [], []

    for chunk in chunks:
        lines = list(filter(None, chunk.split("\n")))

        for row in range(1, len(lines)):
            start, end = lines[:row], lines[row:]

            if len(start) < len(end):
                end = end[: len(start)]
                end = end[::-1]
            else:
                start = start[::-1]
                start = start[: len(end)]

            if count_smudges(start, end) == 1:
                row_splits.append(row)
                break

        for col in range(1, len(lines[0])):
            smudges = 0
            for line in lines:
                start, end = line[:col], line[col:]

                if len(start) < len(end):
                    end = end[: len(start)]
                    end = end[::-1]
                else:
                    start = start[::-1]
                    start = start[: len(end)]

                smudges += count_smudges(start, end)

            if smudges == 1:
                column_splits.append(col)
                break

    answer2 += sum(column_splits)
    answer2 += sum(row_splits) * 100

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
