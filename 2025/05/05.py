import sys
import re

EXAMPLE_INPUT = """
""".strip()


def process_range(all, r):
    out = set()
    [x, y] = r

    to_process = set()
    to_process.add((x, y))

    while to_process:
        (l, h) = to_process.pop()
        use = True

        for ll, hh in all:
            if l >= ll and h <= hh:
                use = False
                break

            if l < ll and h < ll:
                continue

            if l > hh and h > hh:
                continue

            if l <= ll and h >= ll and h <= hh:
                l = l
                h = ll - 1
                continue

            if l <= hh and l >= ll and h >= hh:
                l = hh + 1
                h = h
                continue

            if l <= ll and h >= hh:
                to_process.add((l, ll - 1))
                to_process.add((hh + 1, h))
                use = False

                break

            assert False, "all overlaps covered"

        if use:
            out.add((l, h))

    return out


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    chunks = list(filter(None, input.split("\n\n")))

    lines = list(filter(None, chunks[0].split("\n")))
    ranges = [[int(n) for n in re.findall(r"\d+", line)] for line in lines]

    lines = list(filter(None, chunks[1].split("\n")))
    nums = [[int(n) for n in re.findall(r"\d+", line)] for line in lines]

    # Part 1
    for [num] in nums:
        found = False
        for [l, h] in ranges:
            if num >= l and num <= h:
                found = True

        if found:
            answer1 += 1

    # Part 2
    all = set()
    for [l, h] in ranges:
        processed = process_range(all, [l, h])
        all.update(processed)

    for l, h in all:
        answer2 += h - l + 1

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
