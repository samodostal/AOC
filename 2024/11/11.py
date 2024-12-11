import sys
import re

EXAMPLE_DATA = """
""".strip()


def stones_simulation(loops, map):
    newmap = {}
    for _ in range(loops):
        newmap = {}
        for stone, count in map.items():
            s = str(stone)
            if stone == 0:
                if not newmap.get(1):
                    newmap[1] = 0

                newmap[1] += count
            elif len(s) % 2 == 0:
                l, r = s[: len(s) // 2], s[len(s) // 2 :]

                if not newmap.get(int(l)):
                    newmap[int(l)] = 0
                newmap[int(l)] += count

                if not newmap.get(int(r)):
                    newmap[int(r)] = 0
                newmap[int(r)] += count
            else:
                if not newmap.get(stone * 2024):
                    newmap[stone * 2024] = 0
                newmap[stone * 2024] += count

        map = newmap.copy()

    return sum(newmap.values())


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

    map = {}
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
