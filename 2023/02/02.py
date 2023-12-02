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

    for line in lines:
        x, y = line.split(": ")
        _, id = x.split(" ")
        sets = y.split("; ")

        impossible = False
        red_line = 0
        green_line = 0
        blue_line = 0

        for my_set in sets:
            items = my_set.split(", ")

            red_set = 0
            green_set = 0
            blue_set = 0

            for item in items:
                count, color = item.split(" ")
                count = int(count)
                if color == "red":
                    red_set += count
                    if red_line < count:
                        red_line = count
                elif color == "green":
                    green_set += count
                    if green_line < count:
                        green_line = count
                elif color == "blue":
                    blue_set += count
                    if blue_line < count:
                        blue_line = count

            if red_set > 12 or green_set > 13 or blue_set > 14:
                impossible = True

        answer2 += red_line * green_line * blue_line

        if not impossible:
            answer1 += int(id)

    # Code here

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
