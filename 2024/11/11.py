import sys
import re
from collections import defaultdict

EXAMPLE_DATA = """
""".strip()


def stones_simulation(loops, map):
    for _ in range(loops):
        newmap = defaultdict(int)
        for stone, count in map.items():
            s = str(stone)
            if stone == 0:
                newmap[1] += count
            elif len(s) % 2 == 0:
                l, r = s[: len(s) // 2], s[len(s) // 2 :]
                newmap[int(l)] += count
                newmap[int(r)] += count
            else:
                newmap[stone * 2024] += count

        map = newmap.copy()

    return sum(map.values())


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))
    numbers = [int(n) for n in re.findall(r"-?\d+", lines[0])]

    map = defaultdict(int)
    for stone in numbers:
        map[stone] = 1

    # Part 1
    answer1 = stones_simulation(25, map)

    # Part 2
    answer2 = stones_simulation(75, map)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
