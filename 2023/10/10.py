import sys
import re

EXAMPLE_DATA = """
""".strip()

DIRS = [[0, -1], [1, 0], [0, 1], [-1, 0]]


def pipe_continues_in_dir(pos, dir, map):
    col, row, _ = pos
    new_col, new_row = col + dir[0], row + dir[1]

    if (new_col < 0 or new_col >= len(map[0])) or (new_row < 0 or new_row >= len(map)):
        return False

    if dir == [0, -1]:
        if map[row][col] not in ["|", "J", "L", "S"]:
            return False

        if map[new_row][new_col] in ["F", "7", "|"]:
            return True
        return False

    if dir == [1, 0]:
        if map[row][col] not in ["-", "F", "L", "S"]:
            return False

        if map[new_row][new_col] in ["7", "J", "-"]:
            return True
        return False

    if dir == [0, 1]:
        if map[row][col] not in ["|", "F", "7", "S"]:
            return False

        if map[new_row][new_col] in ["L", "J", "|"]:
            return True
        return False

    if dir == [-1, 0]:
        if map[row][col] not in ["-", "7", "J", "S"]:
            return False

        if map[new_row][new_col] in ["F", "L", "-"]:
            return True
        return False

    assert False


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    s_col = 0
    s_row = 0

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "S":
                s_col = col
                s_row = row

    visited_tiles = []
    unvisited_tiles_with_d = [(s_col, s_row, int(0))]

    while unvisited_tiles_with_d:
        tile = unvisited_tiles_with_d.pop(0)

        for dir in DIRS:
            if pipe_continues_in_dir(tile, dir, lines):
                tile_col, tile_row, tile_distance = tile
                new_col, new_row = tile_col + dir[0], tile_row + dir[1]
                new_tile = (new_col, new_row, tile_distance + 1)

                if (new_col, new_row) not in visited_tiles:
                    unvisited_tiles_with_d.append(new_tile)

        visited_tiles.append((tile[0], tile[1]))
        if tile[2] > answer1:
            answer1 = tile[2]

    # Part 2
    for row, line in enumerate(lines):
        modified_line = line
        for col, char in enumerate(line):
            if (col, row) not in visited_tiles:
                modified_line = modified_line[:col] + "." + modified_line[col + 1 :]

        lines[row] = modified_line

    for line in lines:
        parsed_line = re.sub("F-*7|L-*J", "", line)
        parsed_line = re.sub("F-*J|L-*7", "|", parsed_line)
        outside = True
        for char in parsed_line:
            if char in ["|", "F", "7", "J", "L", "S"]:
                outside = not outside
            if char == "." and not outside:
                answer2 += 1

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
