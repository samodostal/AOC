import sys
from collections import defaultdict

EXAMPLE_DATA = """
""".strip()


def calculate_antidotes(poss, G, repeat):
    antidotes = set()
    for i in range(len(poss)):
        x1, y1 = poss[i]

        for j in range(i + 1, len(poss)):
            x2, y2 = poss[j]
            if x1 == x2 and y1 == y2:
                continue

            dx = x1 - x2
            dy = y1 - y2

            if repeat:
                new1 = (x1 - dx, y1 - dy)
                new2 = (x2 + dx, y2 + dy)

                while G.get(new1) != None:
                    antidotes.add(new1)
                    new1 = (new1[0] + dx, new1[1] + dy)

                while G.get(new2) != None:
                    antidotes.add(new2)
                    new2 = (new2[0] - dx, new2[1] - dy)
            else:
                new1 = (x1 + dx, y1 + dy)
                new2 = (x2 - dx, y2 - dy)

                if G.get(new1) != None:
                    antidotes.add(new1)

                if G.get(new2) != None:
                    antidotes.add(new2)

    return antidotes


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))
    G = defaultdict(lambda: None, {(x, y): lines[y][x] for x in range(len(lines[0])) for y in range(len(lines))})

    D = {}
    for (x, y), char in list(G.items()):
        if char != ".":
            if not D.get(char, None):
                D[char] = []
            D[char].append((x, y))

    # Part 1
    all_antidotes = set()
    for poss in D.values():
        antidotes = calculate_antidotes(poss, G, False)
        all_antidotes.update(antidotes)

    answer1 = len(all_antidotes)

    # Part 2
    all_antidotes = set()
    for poss in D.values():
        antidotes = calculate_antidotes(poss, G, True)
        all_antidotes.update(antidotes)

    answer2 = len(all_antidotes)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
