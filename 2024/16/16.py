import sys
import time
from collections import defaultdict

sys.setrecursionlimit(10000)

# x, y
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

EXAMPLE_INPUT = """
""".strip()


def lowest_score_path_rec(pos, dir, end, dists, score, out, path, min_found, G):
    (x, y) = pos
    (dx, dy) = dir

    if score > min_found[0]:
        return -1

    if score <= dists[(x, y, dx, dy)]:
        dists[(x, y, dx, dy)] = score
    else:
        return -1

    if (x, y) == end:
        tiles = set()
        for p in path:
            tiles.add(p)

        out.append((score, tiles))

        min_found[0] = min(min_found[0], score)
        return score

    sc = float("inf")

    # move forward
    if G[(x + dx, y + dy)] != "#":
        p = path.copy()
        p.append((x + dx, y + dy))
        s = lowest_score_path_rec(
            (x + dx, y + dy), dir, end, dists, score + 1, out, p, min_found, G
        )
        if s != -1:
            sc = min(sc, s)

    # rotate in 2 dirs
    for ddx, ddy in [DIRS[(DIRS.index(dir) + 1) % 4], DIRS[(DIRS.index(dir) - 1) % 4]]:
        if G[(x + ddx, y + ddy)] == "#":
            continue

        s = lowest_score_path_rec(
            (x, y), (ddx, ddy), end, dists, score + 1000, out, path, min_found, G
        )
        if s != -1:
            sc = min(sc, s)

    return sc


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))
    G = defaultdict(
        lambda: "#",
        {(x, y): lines[y][x] for x in range(len(lines[0])) for y in range(len(lines))},
    )

    start = end = (-1, -1)
    dir = (1, 0)

    dists = {}

    start_time = time.time()

    for (x, y), ch in list(G.items()):
        if ch == "S":
            start = (x, y)
        if ch == "E":
            end = (x, y)

        if ch != "#":
            for dx, dy in DIRS:
                dists[(x, y, dx, dy)] = float("inf")

    out = []  # (score, set_path)
    min_found = [float("inf")]
    answer1 = lowest_score_path_rec(
        start, dir, end, dists, 0, out, [start], min_found, G
    )

    min_score = float("inf")
    for score, _ in out:
        if score < min_score:
            min_score = score

    tiles = set()

    for score, set_path in out:
        if score == min_score:
            for p in set_path:
                tiles.add(p)

    answer2 = len(tiles)

    # Takes about 8 minutes  
    print("Time taken: ", time.time() - start_time)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
