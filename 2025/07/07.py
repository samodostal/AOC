import sys
from collections import defaultdict

EXAMPLE_INPUT = """
""".strip()


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))
    G = defaultdict(
        lambda: "O",
        {(x, y): lines[y][x] for x in range(len(lines[0])) for y in range(len(lines))},
    )

    start = (0, 0)
    for key, value in G.items():
        if value == "S":
            start = key

    # Part 1
    beams = {(start[0], start[1] + 1)}

    while beams:
        [bx, by] = beams.pop()

        while G[(bx, by)] == ".":
            G[(bx, by)] = "|"
            by += 1

        if G[(bx, by)] == "^":
            beams.add((bx-1, by))
            beams.add((bx+1, by))
            answer1 += 1

    # Part 2
    col_values = [1 for _ in lines[0]]

    reversed = lines.copy()
    reversed.reverse()

    for line in reversed:
        for i, ch in enumerate(line):
            if ch == "^":
                col_values[i] = col_values[i-1] + col_values[i+1]

    answer2 = max(col_values)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
