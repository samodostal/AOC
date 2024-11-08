import sys

EXAMPLE_DATA = """

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)

""".strip()

Up = (-1, 0)
Right = (0, 1)
Down = (1, 0)
Left = (0, -1)

dirs = [Up, Right, Down, Left]

dirs_match_char = {"U": Up, "R": Right, "D": Down, "L": Left}
dirs_match_int = {3: Up, 0: Right, 1: Down, 2: Left}


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    # direction, distance, color
    instructions = []

    for line in lines:
        direction, distance, color = line.split()
        instructions.append((dirs_match_char[direction], int(distance), color[2:-1]))

    col_pos, row_pos = 0, 0
    min_col_pos, min_row_pos = sys.maxsize, sys.maxsize
    max_col_pos, max_row_pos = 0, 0

    for direction, distance, _ in instructions:
        if direction == Right:
            col_pos += distance
        elif direction == Left:
            col_pos -= distance
        elif direction == Up:
            row_pos -= distance
        elif direction == Down:
            row_pos += distance

        max_col_pos = max(max_col_pos, col_pos)
        max_row_pos = max(max_row_pos, row_pos)
        min_col_pos = min(min_col_pos, col_pos)
        min_row_pos = min(min_row_pos, row_pos)

    cols_count = max_col_pos - min_col_pos + 1
    rows_count = max_row_pos - min_row_pos + 1

    grid = [["." for _ in range(cols_count)] for _ in range(rows_count)]
    pos_row, pos_col = abs(min_row_pos), abs(min_col_pos)

    for direction, distance, _ in instructions:
        next_pos_row, next_pos_col = (
            pos_row + direction[0] * distance,
            pos_col + direction[1] * distance,
        )

        l1, l2 = min(pos_row, next_pos_row), max(pos_row, next_pos_row)
        c1, c2 = min(pos_col, next_pos_col), max(pos_col, next_pos_col)

        for row in range(l1, l2 + 1):
            for col in range(c1, c2 + 1):
                if grid[row][col] == ".":
                    grid[row][col] = "#"
                    answer1 += 1

        pos_row, pos_col = next_pos_row, next_pos_col

    queue = [(pos_row + 1, pos_col + 1)]

    visited = set()

    while queue:
        row, col = queue.pop(0)

        if grid[row][col] == ".":
            grid[row][col] = "#"
            answer1 += 1

        for dir in dirs:
            neighbor_row, neighbor_col = row + dir[0], col + dir[1]

            if (
                neighbor_row < 0
                or neighbor_row >= len(grid)
                or neighbor_col < 0
                or neighbor_col >= len(grid[0])
            ):
                continue

            if (
                grid[neighbor_row][neighbor_col] == "."
                and (neighbor_row, neighbor_col) not in visited
            ):
                queue.append((neighbor_row, neighbor_col))
                visited.add((neighbor_row, neighbor_col))

    # Part 2

    for i, (_, _, color) in enumerate(instructions):
        color_distance, color_direction = color[:5], color[5:]

        distance = int(color_distance, 16)
        direction = dirs_match_int[int(color_direction)]

        instructions[i] = (direction, distance, color)

    points = []

    pos_col, pos_row = 0, 0
    points.append((pos_row, pos_col))

    for direction, distance, _ in instructions:
        next_pos_col, next_pos_row = (
            pos_col + direction[1] * distance,
            pos_row + direction[0] * distance,
        )

        answer2 += distance

        points.append((next_pos_row, next_pos_col))

        pos_col, pos_row = next_pos_col, next_pos_row

    answer2 //= 2
    answer2 += 1

    points_length = len(points)
    sum1, sum2 = 0, 0

    for i in range(0, points_length - 1):
        sum1 += points[i][0] * points[i + 1][1]
        sum2 += points[i][1] * points[i + 1][0]

    sum1 = sum1 + points[points_length - 1][0] * points[0][1]
    sum2 = sum2 + points[0][0] * points[points_length - 1][1]

    answer2 += int(abs(sum1 - sum2) / 2)

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
