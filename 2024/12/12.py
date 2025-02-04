import sys
from collections import defaultdict

EXAMPLE_INPUT = """
""".strip()

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def touching_count(plant, G):
    count = 0
    (x, y) = plant
    for dx, dy in DIRS:
        if G[plant] == G[(x + dx, y + dy)]:
            count += 1

    return count


def get_blank_dirs(plant, zone):
    bds = []
    (x, y) = plant
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in zone:
            bds.append((dx, dy))

    return bds


# Need to search the grid in order, so the neighbors are properly recognized (why I use lines)
def calculate_sides(zone, lines):
    sides = 0
    d = defaultdict(lambda: [])

    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if (x, y) not in zone:
                continue

            blank_dirs = get_blank_dirs((x, y), zone)
            d[(x, y)] = blank_dirs

            for dir in blank_dirs:
                new_side = True
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if dir in d[(nx, ny)]:
                        new_side = False
                        break

                if new_side:
                    sides += 1

    return sides


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
        lambda: ".",
        {(x, y): lines[y][x] for x in range(len(lines[0])) for y in range(len(lines))},
    )

    used = set()

    for (x, y), ch in list(G.items()):
        if (x, y) in used:
            continue

        used.add((x, y))

        stack = [(x, y)]
        zone = []

        while stack:
            px, py = stack.pop()
            zone.append((px, py))
            for dx, dy in DIRS:
                nx, ny = px + dx, py + dy
                if G[(nx, ny)] == ch and (nx, ny) not in used:
                    stack.append((nx, ny))
                    used.add((nx, ny))

        a = len(zone)
        p = sum([4 - touching_count(plant, G) for plant in zone])
        p2 = calculate_sides(zone, lines)

        answer1 += p * a
        answer2 += p2 * a

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
