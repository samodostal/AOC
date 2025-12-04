import sys
from collections import defaultdict

EXAMPLE_INPUT = """
""".strip()

DIRS_DIAGS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


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

    # Part 1
    for (x, y), value in G.items():
        if value != "@":
            continue

        count = 0
        for dx, dy in DIRS_DIAGS:
            if G.get((x + dx, y + dy)) == "@":
                count += 1

        if count < 4:
            answer1 += 1

    # Part 2
    C = G.copy()

    while True:
        for (x, y), value in G.items():
            if value != "@":
                continue

            count = 0

            for dx, dy in DIRS_DIAGS:
                if G.get((x + dx, y + dy)) == "@":
                    count += 1
            if count < 4:
                answer2 += 1
                G[(x, y)] = "X"

        if G == C:
            break

        C = G.copy()

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
