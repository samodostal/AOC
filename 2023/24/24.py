import sys
import re
import z3

EXAMPLE_DATA = """

19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3

""".strip()

# BOUNDARY_LOW, BOUNDARY_HIGH = 7, 27
BOUNDARY_LOW, BOUNDARY_HIGH = 200000000000000, 400000000000000


def same_sign(x, y):
    return (x >= 0) ^ (y < 0)


def do_intersect(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None, None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))
    stones = [[int(i) for i in re.findall("-?\d+", line)] for line in lines]

    for l1 in stones:
        for l2 in stones:
            if l1 == l2:
                continue

            # [[x1, y1], [x2, y2]]
            line1 = [[l1[0], l1[1]], [l1[0] + l1[3], l1[1] + l1[4]]]
            line2 = [[l2[0], l2[1]], [l2[0] + l2[3], l2[1] + l2[4]]]

            (rx, ry) = do_intersect(line1, line2)

            if rx is None or ry is None:
                continue

            d1x = int(rx - line1[0][0])
            d1y = int(ry - line1[0][1])
            d2x = int(rx - line2[0][0])
            d2y = int(ry - line2[0][1])

            in_future = (
                same_sign(d1x, l1[3])
                and same_sign(d1y, l1[4])
                and same_sign(d2x, l2[3])
                and same_sign(d2y, l2[4])
            )

            if not in_future:
                continue

            if (
                rx >= BOUNDARY_LOW
                and rx <= BOUNDARY_HIGH
                and ry >= BOUNDARY_LOW
                and ry <= BOUNDARY_HIGH
            ):
                answer1 += 1

    answer1 /= 2

    # Part 2
    solver = z3.Solver()
    x, y, z = z3.Real("x"), z3.Real("y"), z3.Real("z")
    vx, vy, vz = z3.Real("vx"), z3.Real("vy"), z3.Real("vz")

    for i, (x2, y2, z2, vx2, vy2, vz2) in enumerate(stones[:3]):
        multiplier = z3.Real(f"t{i}")

        solver.add(x + multiplier * vx == x2 + multiplier * vx2)
        solver.add(y + multiplier * vy == y2 + multiplier * vy2)
        solver.add(z + multiplier * vz == z2 + multiplier * vz2)

    solver.check()
    model = solver.model()

    answer2 = sum(model[var].as_long() for var in [x, y, z])

    print("Answer 1: ", int(answer1))
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
