import sys
import math

EXAMPLE_INPUT = """
""".strip()


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    chunks = list(filter(None, input.split("\n\n")))

    for line in list(filter(None, chunks[-1].split("\n"))):
        edges, counts = line.split(": ")

        size = math.prod(map(int, edges.split("x")))
        counts = sum(map(int, counts.split(" ")))

        if counts * 9 <= size:
            answer1 += 1

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
