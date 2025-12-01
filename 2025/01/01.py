import sys
import re

EXAMPLE_INPUT = """
""".strip()


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))

    instr = []
    for line in lines:
        dir = 1 if line[0] == "R" else -1
        val = int(line[1:])
        instr.append((dir, val))

    # Part 1
    dial = 50

    for dir, val in instr:
        dial = (dial + dir * val) % 100
        answer1 += 1 if dial == 0 else 0

    # Part 2
    dial = 50

    for dir, val in instr:
        for i in range(dial, dial + (dir * val), dir):
            answer2 += 1 if i % 100 == 0 else 0

        dial = (dial + dir * val) % 100

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
