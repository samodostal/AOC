import re


def main():
    answer1 = None
    answer2 = None

    file = open("./6.txt")
    data = file.read()
    lines = list(filter(None, data.split("\n")))

    line = lines[0]

    con = 4
    for i in range(con, len(line)):
        if len(set(line[i - con : i])) == con:
            answer1 = i
            break

    con = 14
    for i in range(con, len(line)):
        if len(set(line[i - con : i])) == con:
            answer2 = i
            break

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()

# nums = list(map(int, re.findall(r"\d+", l)))
