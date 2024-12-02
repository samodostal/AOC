import sys
import re

EXAMPLE_DATA = """
""".strip()


def check_safety(numbers):
    incr = False
    decr = False
    in_range = True

    for i in range(1, len(numbers)):
        if numbers[i - 1] > numbers[i]:
            incr = True
        if numbers[i - 1] < numbers[i]:
            decr = True

        if (
            abs(numbers[i - 1] - numbers[i]) == 0
            or abs(numbers[i - 1] - numbers[i]) > 3
        ):
            in_range = False

    if (not incr and not decr) or (incr and decr) or (not in_range):
        return False

    return True


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))
    numbers_per_line = [[int(n) for n in re.findall(r"-?\d+", line)] for line in lines]

    # Part 1
    for numbers in numbers_per_line:
        if check_safety(numbers):
            answer1 += 1

    # Part 2
    for numbers in numbers_per_line:
        one_safe = False

        for i in range(len(numbers)):
            numbers_copy = numbers.copy()
            del numbers_copy[i]

            if check_safety(numbers_copy):
                one_safe = True
                break

        if one_safe:
            answer2 += 1

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
