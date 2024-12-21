import itertools
import sys
import re

EXAMPLE_DATA = """
""".strip()

numpad = {
    "X": (0, 3),
    "A": (2, 3),
    "0": (1, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
}

dirpad = {
    "X": (0, 0),
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

arrow_to_dir = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

memo = {}


def is_valid_path(start, end, steps, pad):
    x, y = pad[start]

    for step in steps:
        dx, dy = arrow_to_dir[step]
        x += dx
        y += dy

        if (x, y) == pad["X"]:
            return False

        if (x, y) == pad[end]:
            return True

    return False


def best_path(start, end, pad, depth):
    global memo

    if memo.get((start, end, depth)):
        return memo[(start, end, depth)]

    sx, sy = pad[start]
    ex, ey = pad[end]

    dx, dy = ex - sx, ey - sy

    if dx == 0 and dy == 0:
        return 1

    steps = ""
    if dx < 0:
        steps += "<" * abs(dx)
    if dx > 0:
        steps += ">" * dx
    if dy < 0:
        steps += "^" * abs(dy)
    if dy > 0:
        steps += "v" * dy

    best_cost = float("inf")

    for current in ["".join(c) + "A" for c in set(itertools.permutations(steps))]:
        if not is_valid_path(start, end, current, pad):
            continue

        if depth == 0:
            current_cost = len(current)
        else:
            current_cost = run(current, dirpad, depth - 1)

        if current_cost < best_cost:
            best_cost = current_cost

    memo[(start, end, depth)] = best_cost

    return best_cost


def run(input, pad, depth):
    input = "A" + input
    total_cost = 0

    for i in range(0, len(input) - 1):
        c1 = input[i]
        c2 = input[i + 1]

        cost = best_path(c1, c2, pad, depth)
        total_cost += cost

    return total_cost


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))

    for line in lines:
        numeric = int(re.findall(r"-?\d+", line)[0])
        size1 = run(line, numpad, 2)
        size2 = run(line, numpad, 25)

        answer1 += numeric * size1
        answer2 += numeric * size2

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
