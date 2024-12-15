import sys
from collections import defaultdict

EXAMPLE_DATA = """
""".strip()

# x, y
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ORDER = ["v", ">", "^", "<"]


def can_move_in_dir_horizontal(pos, dir, G):
    x, y = pos
    dx, dy = dir

    ch = G[(x + dx, y + dy)]

    if ch == "#":
        return False

    if ch == ".":
        return True

    if ch in ["O", "[", "]"]:
        return can_move_in_dir_horizontal((x + dx, y + dy), dir, G)


def can_move_in_dir_vertical(pos, dir, G):
    x, y = pos
    dx, dy = dir

    dch = G[(x + dx, y + dy)]

    if dch == "#":
        return False

    if dch == ".":
        return True

    if dch in ["[", "]"]:
        ddx = 0
        if dch == "]":
            ddx = -1
        else:
            ddx = 1

        return can_move_in_dir_vertical(
            (x + dx, y + dy), dir, G
        ) and can_move_in_dir_vertical((x + dx + ddx, y + dy), dir, G)


def move_in_dir_horizontal(pos, dir, G):
    x, y = pos
    dx, dy = dir

    ch = G[(x, y)]
    dch = G[(x + dx, y + dy)]

    if dch in ["O", "[", "]"]:
        move_in_dir_horizontal((x + dx, y + dy), dir, G)

    if G[(x + dx, y + dy)] == ".":
        G[(x, y)] = "."
        G[(x + dx, y + dy)] = ch


def move_in_dir_vertical(pos, dir, G):
    x, y = pos
    dx, dy = dir

    ch = G[(x, y)]
    dch = G[(x + dx, y + dy)]

    if dch in ["[", "]"]:
        ddx = -1 if dch == "]" else 1
        move_in_dir_vertical((x + dx, y + dy), dir, G)
        move_in_dir_vertical((x + dx + ddx, y + dy), dir, G)

    if G[(x + dx, y + dy)] == ".":
        G[(x, y)] = "."
        G[(x + dx, y + dy)] = ch


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    chunks = list(filter(None, data.split("\n\n")))
    lines = list(filter(None, chunks[0].split("\n")))
    G = defaultdict(
        lambda: "O",
        {(x, y): lines[y][x] for x in range(len(lines[0])) for y in range(len(lines))},
    )
    steps = "".join(chunks[1].split("\n"))
    # Part 1
    pos = (-1, -1)
    for px, py in list(G.keys()):
        if G[(px, py)] == "@":
            pos = (px, py)
            break

    for ins in steps:
        (x, y) = pos
        dir = DIRS[ORDER.index(ins)]
        if can_move_in_dir_horizontal(pos, dir, G):

            move_in_dir_horizontal(pos, dir, G)
            pos = (x + dir[0], y + dir[1])

    for x, y in list(G.keys()):
        if G[(x, y)] == "O":
            answer1 += 100 * y + x

    # Part 2
    lines2 = []
    for line in lines:
        lines2.append("")
        for ch in line:
            nch = {"#": "##", "O": "[]", ".": "..", "@": "@."}[ch]
            lines2[-1] += nch

    G = defaultdict(
        lambda: "O",
        {
            (x, y): lines2[y][x]
            for x in range(len(lines2[0]))
            for y in range(len(lines2))
        },
    )

    pos = (-1, -1)
    for px, py in list(G.keys()):
        if G[(px, py)] == "@":
            pos = (px, py)
            break

    for ins in steps:
        (x, y) = pos
        dir = DIRS[ORDER.index(ins)]
        if ins == ">" or ins == "<":
            if can_move_in_dir_horizontal(pos, dir, G):
                move_in_dir_horizontal(pos, dir, G)
                pos = (x + dir[0], y + dir[1])
        else:
            if can_move_in_dir_vertical(pos, dir, G):
                move_in_dir_vertical(pos, dir, G)
                pos = (x + dir[0], y + dir[1])

    for x, y in list(G.keys()):
        if G[(x, y)] == "[":
            answer2 += 100 * y + x

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
