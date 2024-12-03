import sys
import re

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
    commands_p1 = [n for n in re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)]
    for command in commands_p1:
        [x, y] = [int(n) for n in re.findall(r"-?\d+", command)]
        answer1 += x * y

    # Part 2
    multiply = True

    commands_p2 = [
        n for n in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", data)
    ]
    for command in commands_p2:
        if command == "do()":
            multiply = True
            continue

        if command == "don't()":
            multiply = False
            continue

        if not multiply:
            continue

        [x, y] = [int(n) for n in re.findall(r"-?\d+", str(command))]
        answer2 += x * y

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
