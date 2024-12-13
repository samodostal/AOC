import sys
import re

EXAMPLE_DATA = """
""".strip()

INCREASE = 10000000000000


def solve_det(r):
    ax, ay, bx, by, px, py = r

    A, B, C, D = ax, bx, ay, by

    det = A * D - B * C
    det_x = px * D - py * B
    det_y = A * py - C * px

    cx = int(round(det_x / det))
    cy = int(round(det_y / det))

    if A * cx + B * cy == px and C * cx + D * cy == py:
        return 3 * cx + cy

    return -1


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    chunks = list(filter(None, data.split("\n\n")))

    rounds = []

    for c in chunks:
        a, b, p = list(filter(None, c.split("\n")))
        ax, ay = re.findall(r"-?\d+", a)
        bx, by = re.findall(r"-?\d+", b)
        px, py = re.findall(r"-?\d+", p)

        rounds.append(tuple(map(int, [ax, ay, bx, by, px, py])))

    # Part 1
    for round in rounds:
        out = solve_det(round)
        if out != -1:
            answer1 += out

    # Part 2
    for round in rounds:
        (ax, ay, bx, by, px, py) = round
        round = (ax, ay, bx, by, px + INCREASE, py + INCREASE)

        out = solve_det((ax, ay, bx, by, px + INCREASE, py + INCREASE))
        if out != -1:
            answer2 += out

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
