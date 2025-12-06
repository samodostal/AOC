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
    numbers_per_line = [[int(n) for n in re.findall(r"-?\d+", line)] for line in lines]
    cols = ["" for _ in range(len(lines[0]))]
    for row in lines:
        for i, x in enumerate(row):
            if x == "+" or x == "*" or x == " ":
                continue

            cols[i] += x

    ops = re.findall(r"\*|\+", lines[-1])

    # Part 1
    outs = [1 if x == "*" else 0 for x in ops]
    for numbers in numbers_per_line:
        for i, num in enumerate(numbers):
            if ops[i] == "+":
                outs[i] += num
            if ops[i] == "*":
                outs[i] *= num

    answer1 = sum(outs)

    # Part 2
    outs = [1 if x == "*" else 0 for x in ops]

    i = 0
    for col in cols:
        if col == "":
            i += 1
            continue

        num = int(col)

        if ops[i] == "+":
            outs[i] += num
        if ops[i] == "*":
            outs[i] *= num

    answer2 = sum(outs)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
