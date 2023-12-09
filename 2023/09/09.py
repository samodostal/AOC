import sys
import re

EXAMPLE_DATA = """
""".strip()


def all_zeroes(seq):
    for s in seq:
        if s != 0:
            return False

    return True


def next_in_sequence(seq):
    if all_zeroes(seq):
        return (0, 0)

    next_sequence = []
    for i in range(0, len(seq)):
        if i + 1 < len(seq):
            next_sequence.append(seq[i + 1] - seq[i])

    (next_first, next_last) = next_in_sequence(next_sequence)

    return (seq[0] - next_first, seq[-1] + next_last)


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    sequences = []
    for line in lines:
        sequences.append([int(i) for i in re.findall("-?\d+", line)])

    for sequence in sequences:
        (first, last) = next_in_sequence(sequence)
        answer1 += last
        answer2 += first

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
