from itertools import combinations
import sys
import re
from itertools import combinations

EXAMPLE_INPUT = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()


def is_segment_intersecting_rect(sx1, sy1, sx2, sy2, rx1, ry1, rx2, ry2):
    if sx1 == sx2:
        x_inside = rx1 < sx1 < rx2
        y_overlap = max(sy1, ry1) < min(sy2, ry2)

        return x_inside and y_overlap

    if sy1 == sy2:
        y_inside = ry1 < sy1 < ry2
        x_overlap = max(sx1, rx1) < min(sx2, rx2)

        return y_inside and x_overlap

    return False


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))
    numbers_per_line = [[int(n) for n in re.findall(r"-?\d+", line)] for line in lines]

    # Part 1
    largest_area = 0
    for [x1, y1], [x2, y2] in combinations(numbers_per_line, 2):
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        largest_area = max(largest_area, area)

    answer1 = largest_area

    # Part 2
    segments = []
    points = numbers_per_line.copy()
    points.append(points[0])

    for i in range(0, len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        segments.append((min_x, min_y, max_x, max_y))

    largest_area = 0
    for [x1, y1], [x2, y2] in combinations(numbers_per_line, 2):
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        valid = True
        for xx1, yy1, xx2, yy2 in segments:
            if is_segment_intersecting_rect(
                xx1, yy1, xx2, yy2, min_x, min_y, max_x, max_y
            ):
                valid = False
                break

        if not valid:
            continue

        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        largest_area = max(largest_area, area)

    answer2 = largest_area

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
