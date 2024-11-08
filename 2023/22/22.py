import sys
import re

from functools import cmp_to_key

EXAMPLE_DATA = """

1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9

""".strip()


def compare_by_lowest_z(a, b):
    (_, _, z1, _, _, z2) = a
    (_, _, z3, _, _, z4) = b

    return 1 if min(z1, z2) > min(z3, z4) else -1


def do_overlap(b1, b2):
    (x1, y1, z1, x2, y2, z2) = b1
    (x3, y3, z3, x4, y4, z4) = b2

    overlap_x = (min(x1, x2) <= max(x3, x4)) and (min(x3, x4) <= max(x1, x2))
    overlap_y = (min(y1, y2) <= max(y3, y4)) and (min(y3, y4) <= max(y1, y2))
    overlap_z = (min(z1, z2) <= max(z3, z4)) and (min(z3, z4) <= max(z1, z2))

    return overlap_x and overlap_y and overlap_z


def min_z(brick):
    return min(brick[2], brick[5])


def max_z(brick):
    return max(brick[2], brick[5])


def move_down_by_one(brick):
    (x1, y1, z1, x2, y2, z2) = brick
    return (x1, y1, z1 - 1, x2, y2, z2 - 1)


def can_fall_down(brick, i, bricks):
    brick = move_down_by_one(brick)

    for i in range(max(0, i - 100), i):
        if do_overlap(brick, bricks[i]):
            return False

    return True


def make_brick_fall(brick, i, bricks, start_z):
    (x1, y1, z1, x2, y2, z2) = brick
    z_diff = abs(z1 - z2)
    brick = (x1, y1, start_z, x2, y2, start_z + z_diff)

    while min_z(brick) != 1 and can_fall_down(brick, i, bricks):
        brick = move_down_by_one(brick)

    return brick


def supports_rec(key, dict, visited, graph):
    visited.add(key)

    (supports, supported_by) = dict[key]
    total = 0

    for s in supports:
        (_, sb) = dict[s]
        if all([i in graph for i in sb]) and s not in visited:
            total += 1
            total += supports_rec(s, dict, visited, graph)

    return total


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))
    bricks = []

    for line in lines:
        bricks.append(tuple([int(i) for i in re.findall(r"\d+", line)]))

    bricks_sorted = sorted(bricks, key=cmp_to_key(compare_by_lowest_z))

    highest_z = 0

    for i, brick in enumerate(bricks_sorted):
        bricks_sorted[i] = make_brick_fall(brick, i, bricks_sorted, highest_z + 1)
        highest_z = max(highest_z, max_z(bricks_sorted[i]))

    dict = {}

    for i, b1 in enumerate(bricks_sorted):
        supports = set()
        supported_by = set()

        (x1, y1, z1, x2, y2, z2) = b1
        b1l = min_z(b1)
        b1h = max_z(b1)

        for j, b2 in enumerate(bricks_sorted):
            b2l = min_z(b2)
            b2h = max_z(b2)

            if b1h + 1 == b2l and do_overlap(b2, (x1, y1, z1 + 1, x2, y2, z2 + 1)):
                supports.add(j)

            if b1l - 1 == b2h and do_overlap(
                b2, (x1, y1, max(0, z1 - 1), x2, y2, max(0, z2 - 1))
            ):
                supported_by.add(j)

        dict[i] = (supports, supported_by)

    # Part 1
    for supports, supported_by in dict.values():
        can_remove = True

        for s in supports:
            (_, sb) = dict[s]
            if len(sb) == 1:
                can_remove = False
                break

        if can_remove:
            answer1 += 1

    # Part 2
    for key, (supports, supported_by) in dict.items():
        graph = set()
        graph.add(key)

        queue = list(supports)
        while queue:
            s = queue.pop(0)
            if s in graph:
                continue

            if not all([i in graph for i in dict[s][1]]):
                continue

            graph.add(s)
            queue.extend(dict[s][0])

        count = supports_rec(key, dict, set(), graph)
        answer2 += count

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
