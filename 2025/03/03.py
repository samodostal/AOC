import sys

EXAMPLE_INPUT = """
""".strip()


def max_in_range(min, max, arr):
    out, index = 0, 0
    for i in range(min, max):
        if arr[i] > out:
            out = arr[i]
            index = i

    return (out, index)


def max_digits(arr, count):
    out = ""
    min, max = 0, 0

    for i in range(count):
        max = len(arr) - (count - i) + 1

        dig, index = max_in_range(min, max, arr)
        out += str(dig)
        min = index + 1

    return int(out)


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))

    banks = []
    for line in lines:
        banks.append([int(num) for num in line])

    # Part 1 and 2
    for bank in banks:
        answer1 += max_digits(bank, 2)
        answer2 += max_digits(bank, 12)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
