import re
import functools


def compare(lower, higher):
    if type(lower) == int and type(higher) == int:
        if lower == higher:
            return 0
        elif lower < higher:
            return -1
        else:
            return 1

    if type(lower) == int and type(higher) == list:
        lower = [lower]
    elif type(lower) == list and type(higher) == int:
        higher = [higher]

    assert type(lower) == list and type(higher) == list

    if type(lower) == list and type(higher) == list:
        for i in range(min(len(lower), len(higher))):
            compared = compare(lower[i], higher[i])
            if compared == -1:
                return -1
            elif compared == 1:
                return 1

        if len(lower) == len(higher):
            return 0
        elif len(lower) < len(higher):
            return -1
        else:
            return 1


def main():
    answer1 = None
    answer2 = None

    file = open("./13.txt")
    data = file.read()
    lines = list(filter(None, data.split("\n")))
    chunks = list(filter(None, data.split("\n\n")))

    index = 0
    sum = 0

    all_lines = [[[2]], [[6]]]

    for chunk in chunks:
        lines = []
        for line in list(filter(None, chunk.split("\n"))):
            evaled = eval(line)
            all_lines.append(evaled)
            lines.append(evaled)
        index += 1

        assert len(lines) == 2
        compared = compare(lines[0], lines[1])
        if compared == 1:
            sum += index

    all_sorted = sorted(all_lines, key=functools.cmp_to_key(compare))

    indices = []

    for i, x in enumerate(all_sorted):
        if x == [[2]] or x == [[6]]:
            indices.append(i + 1)

    answer1 = sum
    answer2 = indices[0] * indices[1]

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
