import sys

EXAMPLE_DATA = """
""".strip()


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    chunks = list(filter(None, data.split("\n\n")))
    lines = list(filter(None, data.split("\n")))

    locks = set()
    keys = set()

    for chunk in chunks:
        lines = list(filter(None, chunk.split("\n")))
        heights = [-1 for _ in range(5)]

        for line in lines:
            for i, x in enumerate(line):
                heights[i] += 1 if x == "#" else 0

        if lines[0] == "#####":
            locks.add(tuple(heights))
        else:
            keys.add(tuple(heights))

    for lock in locks:
        for key in keys:
            do_fit = True

            for i in range(5):
                if lock[i] + key[i] > 5:
                    do_fit = False
                    break

            if do_fit:
                answer1 += 1

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
