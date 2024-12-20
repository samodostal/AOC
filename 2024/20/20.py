import sys
from collections import defaultdict

EXAMPLE_DATA = """
""".strip()

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def flood_fill(start, dists, G):
    q = [(0, start)]

    while q:
        (d, pos) = q.pop(0)
        x, y = pos

        if pos in dists and d >= dists[pos]:
            continue

        dists[pos] = d

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy

            if G[(nx, ny)] != "#":
                q.append((d + 1, (nx, ny)))


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))
    G = defaultdict(
        lambda: "#",
        {(x, y): lines[y][x] for x in range(len(lines[0])) for y in range(len(lines))},
    )

    dists = {}
    start = end = (-1, -1)

    for (x, y), ch in list(G.items()):
        start = (x, y) if ch == "S" else start
        end = (x, y) if ch == "E" else end

    flood_fill(start, dists, G)

    time = dists[end]

    for (x1, y1), d1 in dists.items():
        for (x2, y2), d2 in dists.items():
            if (x1, y1) == (x2, y2):
                continue

            dist = abs(x1 - x2) + abs(y1 - y2)

            if dist == 2:
                shortcut_time = time - abs(d1 - d2) - 1 + dist
                if time - shortcut_time >= 100:
                    answer1 += 1

            if dist <= 20:
                shortcut_time = time - abs(d1 - d2) - 1 + dist
                if time - shortcut_time >= 100:
                    answer2 += 1

    answer1 //= 2
    answer2 //= 2

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
