import sys
import itertools

EXAMPLE_DATA = """
""".strip()


def can_be_solved(expected, nums, include_or):
    ops_combinations = itertools.product(["+", "*", "||"], repeat=len(nums) - 1)

    for op in ops_combinations:
        res = nums[0]
        for i, op in enumerate(op):
            if op == "+":
                res += nums[i + 1]
            elif op == "*":
                res *= nums[i + 1]
            elif include_or and op == "||":
                res = int(str(res) + str(nums[i + 1]))

        if res == expected:
            return True

    return False


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))

    D = {}
    for line in lines:
        res, nums = line.split(": ")
        D[int(res)] = list(filter(None, map(int, nums.split(" "))))

    # Part 1
    for res, nums in D.items():
        if can_be_solved(res, nums, False):
            answer1 += res

    # Part 2
    for res, nums in D.items():
        if can_be_solved(res, nums, True):
            answer2 += res

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
