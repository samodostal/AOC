import collections

letters = ["S"] + [chr(i) for i in range(ord("a"), ord("z") + 1)] + ["E"]

DIR_ADDERS = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def bfs(matrix, start, end):
    queue = collections.deque([start])
    used = set(start)
    distances = {start: 0}

    while queue:
        tile = queue.popleft()
        for dir in DIR_ADDERS:
            neighbor = (tile[0] + dir[0], tile[1] + dir[1])
            if (
                not is_in_bounds(*neighbor, matrix)
                or neighbor in used
                or matrix[neighbor[1]][neighbor[0]]
                not in letters[
                    0 : letters.index(matrix[tile[1]][tile[0]]) + 2
                ]
            ):
                continue

            used.add(neighbor)
            queue.append(neighbor)
            distances[neighbor] = distances[tile] + 1

            if neighbor == end:
                return distances[tile] + 1

    return distances


def is_in_bounds(x, y, matrix):
    return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)


def main():
    answer1 = None
    answer2 = None

    file = open("./12.txt")
    data = file.read()
    lines = list(filter(None, data.split("\n")))

    matrix = []
    letters_a = []
    start = None
    end = None

    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            pos = (x, y)
            if char == "S":
                start = pos
                letters_a.append(pos)
            elif char == "E":
                end = pos
            elif char == "a":
                letters_a.append(pos)

            row.append(char)
        matrix.append(row)

    assert start is not None and end is not None

    distance_end = bfs(matrix, start, end)

    lowest_a_distance = -1

    for pos_a in letters_a:
        distance = bfs(matrix, pos_a, end)

        if lowest_a_distance == -1:
            lowest_a_distance = distance
            continue

        if type(distance) == int:
            lowest_a_distance = min(lowest_a_distance, distance)

    answer1 = distance_end
    answer2 = lowest_a_distance

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
