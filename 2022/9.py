import re

UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3

DIR_ADDERS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

dir_map = {"U": UP, "R": RIGHT, "L": LEFT, "D": DOWN}


def are_adjacent(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def update_tail(hx, hy, tx, ty):
    if are_adjacent(hx, hy, tx, ty):
        return tx, ty

    diff_x = hx - tx
    diff_y = hy - ty
    if diff_x != 0:
        tx += diff_x // abs(diff_x)
    if diff_y != 0:
        ty += diff_y // abs(diff_y)

    return tx, ty


def main():
    answer1 = None
    answer2 = None

    file = open("./9.txt")
    data = file.read()
    lines = list(filter(None, data.split("\n")))

    visited1 = set()
    visited2 = set()
    tails = [[0, 0] for _ in range(10)]

    for line in lines:
        sp = line.split()
        dir = dir_map.get(sp[0])
        for i in range(int(sp[1])):
            tails[0][0] += DIR_ADDERS[dir][0]
            tails[0][1] += DIR_ADDERS[dir][1]

            for i in range(len(tails) - 1):
                tx, ty = update_tail(
                    tails[i][0],
                    tails[i][1],
                    tails[i + 1][0],
                    tails[i + 1][1],
                )

                tails[i + 1] = [tx, ty]

            visited1.add((tails[1][0], tails[1][1])) # first is head
            visited2.add((tails[-1][0], tails[-1][1]))

    answer1 = len(visited1)
    answer2 = len(visited2)

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()

# nums = list(map(int, re.findall(r"\d+", l)))
