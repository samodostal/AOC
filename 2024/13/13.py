import sys
import re

EXAMPLE_DATA = """
""".strip()

INCREASE = 10000000000000


def solve(r, max):
    ax, ay, bx, by, px, py = r
    for a in range(max, 1, -1):
        for b in range(max, 1, -1):
            fx = a * ax + b * bx == px
            fy = a * ay + b * by == py
            if fx and fy:
                return a * 3 + b * 1

    return -1


def solve2(r):
    ax, ay, bx, by, px, py = r

    A, B, C, D = ax, bx, ay, by
    det = 1 / (A * D - B * C)

    AA, BB, CC, DD = (D * det), (-B * det), (-C * det), (A * det)

    cx = int(round(AA * px + BB * py))
    cy = int(round(CC * px + DD * py))

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
        out = solve(round, 100)
        if out != -1:
            answer1 += out

    # Part 2
    for round in rounds:
        (ax, ay, bx, by, px, py) = round

        round = (ax, ay, bx, by, px + INCREASE, py + INCREASE)

        out = solve2(round)
        if out != -1:
            answer2 += out

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
