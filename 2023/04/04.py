import sys
import re

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

    lines = list(filter(None, data.split("\n")))

    dict = {}

    for line in lines:
        index = line.split(": ")[0].split()[1]
        dict[int(index)] = 1

    for line in lines:
        prefix, body = line.split(": ")
        index = int(prefix.split()[1])

        s_winning, s_yours = body.split(" | ")
        winning = re.findall("[0-9]+", s_winning)
        yours = re.findall("[0-9]+", s_yours)

        answer2 += dict[index]

        x = sum([1 for i in yours if i in winning])

        answer1 += 2 ** (x - 1) if x > 0 else 0

        for i in range(index + 1, index + x + 1):
            dict[i] += dict[index]

    # Code here

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
