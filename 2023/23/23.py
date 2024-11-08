import sys

sys.setrecursionlimit(10000)

EXAMPLE_DATA = """

#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#

""".strip()

North = (-1, 0)
East = (0, 1)
South = (1, 0)
West = (0, -1)

dirs = [North, East, South, West]
char_to_dir_map = {"^": North, ">": East, "v": South, "<": West}


def neighbors(position, lines):
    output = set()
    row, col = position

    for drow, dcol in dirs:
        nrow, ncol = row + drow, col + dcol

        if lines[nrow][ncol] in [".", ">", "v", "<", "^"]:
            output.add((nrow, ncol))

    return output


def dfs_longest_path(current, end, path, visited, paths, lines, p2):
    row, col = current

    if current == end:
        paths.add(path)
        return 0

    if not p2:
        if lines[row][col] != ".":
            drow, dcol = char_to_dir_map[lines[row][col]]
            neighbor = row + drow, col + dcol

            if neighbor in visited:
                return 0

            visited.add(neighbor)
            return dfs_longest_path(
                neighbor, end, path + 1, visited.copy(), paths, lines, p2
            )

    for neighbor in neighbors(current, lines):
        row, col = neighbor

        if neighbor in visited:
            continue

        visited.add(neighbor)
        dfs_longest_path(neighbor, end, path + 1, visited.copy(), paths, lines, p2)

    return 0


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    # (row, col)
    start = (0, 1)
    end = (len(lines) - 1, len(lines[0]) - 2)

    paths_p1 = set()
    paths_p2 = set()

    dfs_longest_path(start, end, 0, set(), paths_p1, lines, False)
    dfs_longest_path(start, end, 0, set(), paths_p2, lines, True)

    answer1 = max(paths_p1)
    answer2 = max(paths_p2)

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
