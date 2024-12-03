import sys
import re
import math

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

    # Part 1
    commands_p1 = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    for command in commands_p1:
        answer1 += math.prod([int(n) for n in re.findall(r"-?\d+", command)])

    # Part 2
    multiply = True

    commands_p2 = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", data)
    for command in commands_p2:
        if command == "do()":
            multiply = True
            continue

        if command == "don't()":
            multiply = False
            continue

        if not multiply:
            continue

        answer2 += math.prod([int(n) for n in re.findall(r"-?\d+", str(command))])

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
