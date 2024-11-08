import sys
import math

EXAMPLE_DATA = """
""".strip()


def count_cycles(current, directions, dict):
    cycles = 0

    while current[2] != "Z":
        dir = directions[cycles % len(directions)]
        if dir == "L":
            current = dict[current][0]
        elif dir == "R":
            current = dict[current][1]

        cycles += 1

    return cycles


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    chunks = list(filter(None, data.split("\n\n")))

    [directions, data] = chunks
    dict = {}

    for line in data.split("\n"):
        if not line:
            continue

        start, end = line.split(" = ")
        left, right = end.split(", ")
        left = left[1:]
        right = right[:-1]

        dict[start] = [left, right]

    # Part 1
    current = "AAA"
    i = 0

    while current[2] != "Z":
        dir = directions[i]
        current = dict[current][0 if dir == "L" else 1]

        i = (i + 1) % len(directions)
        answer1 += 1

    # Part 2
    current_nodes = [node for node in dict.keys() if node[2] == "A"]
    counts = []

    for node in current_nodes:
        counts.append(count_cycles(node, directions, dict))

    answer2 = math.lcm(*counts)

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
