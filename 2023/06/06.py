import sys
import re

EXAMPLE_DATA = """
""".strip()


def main():
    answer1 = 1
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    times = [int(i) for i in re.findall("[0-9]+", lines[0])]
    distances = [int(i) for i in re.findall("[0-9]+", lines[1])]

    time_big = int("".join(re.findall("[0-9]+", lines[0])))
    distance_big = int("".join(re.findall("[0-9]+", lines[1])))

    for i in range(len(times)):
        max_speed = times[i]
        distance = distances[i]
        x = 0

        for speed in range(max_speed):
            simulated_distance = speed * (max_speed - speed)
            if simulated_distance > distance:
                x += 1

        answer1 *= x

    for max_speed in range(time_big):
        simulated_distance = max_speed * (time_big - max_speed)
        if simulated_distance > distance_big:
            answer2 += 1

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
