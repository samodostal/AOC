import sys
import re

EXAMPLE_INPUT = """
""".strip()


def check_safety(numbers):
    inc, dec = False, False
    in_range = True

    for i in range(1, len(numbers)):
        if numbers[i - 1] > numbers[i]:
            inc = True
        if numbers[i - 1] < numbers[i]:
            dec = True

        diff = abs(numbers[i - 1] - numbers[i])
        if diff == 0 or diff > 3:
            in_range = False

    return inc ^ dec and in_range


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

    # Part 1
    for numbers in numbers_per_line:
        if check_safety(numbers):
            answer1 += 1

    # Part 2
    for numbers in numbers_per_line:
        for i in range(len(numbers)):
            numbers_copy = numbers.copy()
            del numbers_copy[i]

            if check_safety(numbers_copy):
                answer2 += 1
                break

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
