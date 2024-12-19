import sys

EXAMPLE_DATA = """
""".strip()


def can_be_made_rec(target, patterns, memo):
    if target == "":
        return 1

    if memo.get(target):
        return memo[target]

    sum = 0
    for p in patterns:
        if len(target) >= len(p) and target.startswith(p):
            sum += can_be_made_rec(target[len(p) :], patterns, memo)

    memo[target] = sum
    return sum


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    chunks = list(filter(None, data.split("\n\n")))

    patterns = chunks[0].split(", ")
    targets = list(filter(None, chunks[1].split("\n")))

    # Part 1 and 2
    for target in targets:
        answer1 += can_be_made_rec(target, patterns, {}) != 0
        answer2 += can_be_made_rec(target, patterns, {})

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
