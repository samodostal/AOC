import sys

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
    chunks = list(filter(None, data.split("\n\n")))

    rules = set()
    orders = []

    for rule in list(filter(None, chunks[0].split("\n"))):
        [x, y] = rule.split("|")
        rules.add((x, y))

    for order in list(filter(None, chunks[1].split("\n"))):
        orders.append(list(filter(None, order.split(","))))

    incorrect = []

    # Part 1
    for order in orders:
        is_valid = True
        for i in range(1, len(order)):
            if (order[i], order[i - 1]) in rules:
                is_valid = False
                break

        if is_valid:
            middle = order[int(len(order) / 2)]
            answer1 += int(middle)
        else:
            incorrect.append(order)

    # Part 2
    for nums in incorrect:
        try_again = True
        while try_again:
            try_again = False
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if (nums[j], nums[i]) in rules:
                        nums[i], nums[j] = nums[j], nums[i]
                        try_again = True

    for order in incorrect:
        middle = order[int(len(order) / 2)]
        answer2 += int(middle)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
