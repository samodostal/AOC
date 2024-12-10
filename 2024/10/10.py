import sys
from collections import defaultdict

EXAMPLE_DATA = """
""".strip()

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def calc_bfs(start, G):
    out = 0
    queue = [start]
    visited = set()

    while queue:
        p = queue.pop()
        (x, y) = p
        if p not in visited:
            visited.add(p)
            if G[p] == "9":
                out += 1

            for pn in [(x + dx, y + dy) for (dx, dy) in DIRS]:
                if not G[pn].isdigit() or pn in visited:
                    continue

                if int(G[pn]) == int(G[p]) + 1:
                    queue.append(pn)

    return out


def calc_dfs(start, G):
    if G[start] == "9":
        return 1

    out = 0
    (x, y) = start

    for pn in [(x + dx, y + dy) for (dx, dy) in DIRS]:
        if G[pn].isdigit() and int(G[pn]) == int(G[start]) + 1:
            out += calc_dfs(pn, G)

    return out


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
        lambda: "O",
        {(x, y): lines[y][x] for x in range(len(lines[0])) for y in range(len(lines))},
    )

    starts = []
    for (x, y), char in list(G.items()):
        if char == "0":
            starts.append((x, y))

    # Part 1
    for start in starts:
        answer1 += calc_bfs(start, G)

    # Part 2
    for start in starts:
        answer2 += calc_dfs(start, G)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
