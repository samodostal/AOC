import sys
import math
import re
from collections import defaultdict

EXAMPLE_DATA = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()

# W, H = 11, 7
W, H = 101, 103


def get_quadrants_count(poss):
    q1, q2, q3, q4 = 0, 0, 0, 0

    for x in range(int((W - 1) / 2)):
        for y in range(int((H - 1) / 2)):
            q1 += sum([(x, y) in pos for pos in poss.values()])

    for x in range(int((W + 1) / 2), W):
        for y in range(int((H - 1) / 2)):
            q2 += sum([(x, y) in pos for pos in poss.values()])

    for x in range(int((W - 1) / 2)):
        for y in range(int((H + 1) / 2), H):
            q3 += sum([(x, y) in pos for pos in poss.values()])

    for x in range(int((W + 1) / 2), W):
        for y in range(int((H + 1) / 2), H):
            q4 += sum([(x, y) in pos for pos in poss.values()])

    return q1, q2, q3, q4


def print_grid(poss):
    for y in range(H):
        for x in range(W):
            print("#" if (x, y) in poss.values() else ".", end="")
        print()


def all_separate(poss):
    for i, (x1, y1) in enumerate(poss.values()):
        for j, (x2, y2) in enumerate(poss.values()):
            if i != j and x1 == x2 and y1 == y2:
                return False

    return True


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))
    numbers_per_line = [[int(n) for n in re.findall(r"-?\d+", line)] for line in lines]

    # Part 1
    poss = {}

    for i, (x, y, vx, vy) in enumerate(numbers_per_line):
        poss[i] = []
        px, py = x, y
        for _ in range(100):
            px = (px + vx) % W
            py = (py + vy) % H

        poss[i].append((px, py))

    qs = get_quadrants_count(poss)

    answer1 = math.prod(qs)

    # Part 2
    poss = {}
    for s in range(1, 10000):
        for i, (x, y, vx, vy) in enumerate(numbers_per_line):
            px, py = x, y
            if poss.get(i):
                px, py = poss[i]

            px = (px + vx) % W
            py = (py + vy) % H

            poss[i] = (px, py)

        if s % 1000 == 0:
            print("Searching: ", s)

        if all_separate(poss):
            # print_grid(poss)
            answer2 = s
            break

    print()
    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
