import sys

EXAMPLE_INPUT = """
""".strip()


def paths(g, current, end, memo):
    if (current, end) in memo:
        return memo[(current, end)]

    if current == end:
        return 1

    if current == "out":
        return 0

    sum = 0
    for n in g[current]:
        sum += paths(g, n, end, memo)

    memo[(current, end)] = sum
    return sum


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))
    splits_per_line = [line.split() for line in lines]

    g = {}
    for s in splits_per_line:
        g[s[0][:-1]] = s[1:]

    # Part 1
    answer1 = paths(g, "you", "out", {})

    # Part 2
    memo = {}

    dac_first_paths = (
        paths(g, "svr", "dac", memo)
        * paths(g, "dac", "fft", memo)
        * (paths(g, "fft", "out", memo))
    )
    fft_first_paths = (
        paths(g, "svr", "fft", memo)
        * paths(g, "fft", "dac", memo)
        * (paths(g, "dac", "out", memo))
    )
    answer2 = dac_first_paths + fft_first_paths

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
