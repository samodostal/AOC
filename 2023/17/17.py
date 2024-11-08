import sys
import heapq

EXAMPLE_DATA = """
""".strip()

North = (-1, 0)
East = (0, 1)
South = (1, 0)
West = (0, -1)

dirs = [North, East, South, West]


def calculate_distance(map, min_steps, max_steps):
    start_pos = (0, 0)
    end_pos = (len(map) - 1, len(map[0]) - 1)

    queue = [(0, *start_pos, 0, 0)]
    visited = set()

    while queue:
        distance, row, col, d_row, d_col = heapq.heappop(queue)

        if (row, col) == end_pos:
            return distance

        if (row, col, d_row, d_col) in visited:
            continue

        for dir_row, dir_col in dirs:
            if (dir_row, dir_col) == (d_row, d_col) or (dir_row, dir_col) == (
                -d_row,
                -d_col,
            ):
                continue

            t_distance = distance
            t_row = row
            t_col = col

            for steps in range(1, max_steps + 1):
                t_row, t_col = t_row + dir_row, t_col + dir_col

                if t_row < 0 or t_row >= len(map) or t_col < 0 or t_col >= len(map[0]):
                    continue

                t_distance += int(map[t_row][t_col])

                if steps >= min_steps:
                    heapq.heappush(queue, (t_distance, t_row, t_col, dir_row, dir_col))

        visited.add((row, col, d_row, d_col))


def all_neighbors(node, map):
    neighbors = []
    row, col, _, node_dir = node

    for dir in dirs:
        new_row = row + dir[0]
        new_col = col + dir[1]

        if dir == (node_dir[0] * (-1), node_dir[1] * (-1)):
            continue

        if new_row < 0 or new_row >= len(map):
            continue

        if new_col < 0 or new_col >= len(map[0]):
            continue

        neighbors.append((new_row, new_col, dir))

    return neighbors


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    answer1 = calculate_distance(lines, 1, 3)
    answer2 = calculate_distance(lines, 4, 10)

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
