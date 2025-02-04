import sys
import math
import re

EXAMPLE_INPUT = """
""".strip()

# W, H = 11, 7
W, H = 101, 103


def quadrants(poss):
    qs = [0, 0, 0, 0]

    for x in range(int((W - 1) / 2)):
        for y in range(int((H - 1) / 2)):
            qs[0] += sum([[x, y] == pos for pos in poss])

    for x in range(int((W + 1) / 2), W):
        for y in range(int((H - 1) / 2)):
            qs[1] += sum([[x, y] == pos for pos in poss])

    for x in range(int((W - 1) / 2)):
        for y in range(int((H + 1) / 2), H):
            qs[2] += sum([[x, y] == pos for pos in poss])

    for x in range(int((W + 1) / 2), W):
        for y in range(int((H + 1) / 2), H):
            qs[3] += sum([[x, y] == pos for pos in poss])

    return qs


def print_grid(poss):
    for y in range(H):
        for x in range(W):
            print("#" if [x, y] in poss else ".", end="")
        print()


def all_separate(poss):
    for i, [x1, y1] in enumerate(poss):
        for j, [x2, y2] in enumerate(poss):
            if i != j and x1 == x2 and y1 == y2:
                return False

    return True


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))
    robots = [[int(n) for n in re.findall(r"-?\d+", line)] for line in lines]
    robots2 = robots.copy()

    # Part 1
    for _ in range(100):
        robots = [[(x + vx) % W, (y + vy) % H, vx, vy] for [x, y, vx, vy] in robots]

    answer1 = math.prod(quadrants([[x, y] for [x, y, _, _] in robots]))

    # Part 2
    for s in range(1, 10000):
        robots2 = [[(x + vx) % W, (y + vy) % H, vx, vy] for [x, y, vx, vy] in robots2]

        if s % 1000 == 0:
            print("Searching: ", s)

        if all_separate([[x, y] for [x, y, _, _] in robots2]):
            # print_grid(poss)
            answer2 = s
            break

    print()
    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
