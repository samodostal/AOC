import sys
from collections import defaultdict

EXAMPLE_INPUT = """
""".strip()

# x, y
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def simulate_with_loops(pos, dir, D):
    visited = set()

    while D[pos] != "O":
        if (pos, dir) in visited:
            return True  # loop found

        (x, y), (dx, dy) = pos, dir
        visited.add((pos, dir))

        if D[(x + dx, y + dy)] == "#":
            dir = DIRS[(DIRS.index(dir) + 1) % 4]
        else:
            pos = (x + dx, y + dy)

    return False  # loop not found, escaped


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    grid = list(filter(None, input.split("\n")))

    start_pos = pos = (0, 0)
    start_dir = dir = DIRS[3]

    D = defaultdict(lambda: "O")
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            D[(x, y)] = grid[x][y]

            if D[(x, y)] == "^":
                pos = start_pos = (x, y)

    # Part 1
    path = []

    while D[pos] != "O":
        path.append(pos)
        (x, y), (dx, dy) = pos, dir

        if D[(x + dx, y + dy)] == "#":
            dir = DIRS[(DIRS.index(dir) + 1) % 4]
        else:
            pos = (x + dx, y + dy)

    answer1 = len(set(path))

    # Part 2
    obstacles = set()
    for x, y in path[1:]:
        D[x, y] = "#"

        if simulate_with_loops(start_pos, start_dir, D):
            obstacles.add((x, y))

        D[x, y] = "."

    answer2 = len(obstacles)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
