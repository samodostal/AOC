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
    lines = list(filter(None, data.split("\n")))

    for line in lines:
        digits = re.findall("[0-9]", line)
        answer1 += int(digits[0]) * 10 + int(digits[-1])

    for line in lines:
        for i, num in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        ):
            line = line.replace(num, num + str(i + 1) + num)

        digits = re.findall("[0-9]", line)
        answer2 += int(digits[0]) * 10 + int(digits[-1])

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
