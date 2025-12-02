import sys

EXAMPLE_INPUT = """
""".strip()


def is_invalid_by_index(sid, i):
    if not i.is_integer():
        return False

    i = int(i)
    s = set()

    while len(sid) > 0:
        s.add(sid[0:i])
        sid = sid[i:]

    return len(s) == 1


def is_invalid(sid):
    for index in range(1, len(sid) // 2 + 1):
        if is_invalid_by_index(sid, index):
            return True

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

    # Part 1 and 2
    for ranges in lines[0].split(","):
        [x, y] = map(int, ranges.split("-"))

        for id in range(x, y + 1):
            sid = str(id)

            answer1 += id if is_invalid_by_index(sid, len(sid) / 2) else 0
            answer2 += id if is_invalid(sid) else 0

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
