import sys

DIRS = [(0, 1), (-1, 1), (1, 1)]


def intersects_vertices(pos, vertices):
    x, y = pos
    for vertex in vertices:
        p1, p2 = vertex
        x1, y1 = p1
        x2, y2 = p2

        if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(
            y1, y2
        ):
            return True

    return False


def fall_sand(pos, fallen, vertices, bottom):
    x, y = pos
    for dir in DIRS:
        poss_x = x + dir[0]
        poss_y = y + dir[1]

        if (poss_x, poss_y) in fallen or intersects_vertices(
            (poss_x, poss_y), vertices
        ):
            continue

        return fall_sand((poss_x, poss_y), fallen, vertices, bottom)

    if x == 500 and y == 0:
        return None
    return pos


def main():
    answer1 = None
    answer2 = None

    file = open("./14.txt")
    data = file.read()
    lines = list(filter(None, data.split("\n")))

    fallen_sand = set()
    vertices = set()
    bottom = 0
    count = 0

    for line in lines:
        points = []
        for pos in line.split(" -> "):
            count += 1
            evaled = eval(pos)
            x, y = evaled
            bottom = max(bottom, y)
            points.append(evaled)

        for i in range(len(points) - 1):
            vertices.add((points[i], points[i + 1]))

    vertices.add(((-sys.maxsize, bottom + 2), (sys.maxsize, bottom + 2)))

    i = 0

    while True:
        sand = fall_sand((500, 0), fallen_sand, vertices, bottom)
        fallen_sand.add(sand)
        i += 1
        print(i)
        if sand is None:
            break

    answer2 = len(fallen_sand) + 1

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2) # runs for about 3 minutes


if __name__ == "__main__":
    main()
