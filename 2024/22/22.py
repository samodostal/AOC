import sys
import re

sys.setrecursionlimit(10000)

EXAMPLE_INPUT = """
""".strip()


def secret_fn(num):
    x = num << 6
    num ^= x
    num %= 16777216

    x = round(num >> 5)
    num ^= x
    num %= 16777216

    x = num * 2048
    num ^= x
    num %= 16777216

    return num


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
    for [num] in numbers_per_line:
        x = num
        for _ in range(2000):
            x = secret_fn(x)

        answer1 += x

    ends = []

    # Part 2
    for [num] in numbers_per_line:
        ends.append([num % 10])
        x = num
        for _ in range(2000):
            x = secret_fn(x)
            ends[-1].append(x % 10)

    D = {}
    for nums in ends:
        dd = {}
        for i in range(1, len(nums) - 3):
            s = nums[i - 1]
            a, b, c, d = nums[i], nums[i + 1], nums[i + 2], nums[i + 3]
            x, y, z, w = a - s, b - a, c - b, d - c

            if not dd.get((x, y, z, w)):
                dd[(x, y, z, w)] = d

        for key, value in dd.items():
            if not D.get(key):
                D[key] = []

            D[key].append(value)

    answer2 = max([sum(x) for x in list(D.values())])

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
