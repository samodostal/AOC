def to_ord_set(my_set):
    total = 0
    for e in my_set:
        if e.islower():
            total += ord(e) - ord("a") + 1
        else:
            total += ord(e) - ord("A") + 27
    return total


def my_div(string: str):
    return {x for x in string}


def main():
    answer1 = None
    answer2 = None

    file = open("./3.txt")
    data = file.read()
    lines = data.split("\n")

    total1 = 0
    for line in lines:
        first_halve = line[:len(line) // 2]
        second_halve = line[len(line) // 2:]

        first = my_div(first_halve)
        second = my_div(second_halve)

        total1 += to_ord_set(first.intersection(second))

    total2 = 0
    i = 0
    while i < len(lines):
        if not lines[i]:
            break

        line1 = my_div(lines[i])
        line2 = my_div(lines[i + 1])
        line3 = my_div(lines[i + 2])

        intersection = line1.intersection(line2.intersection(line3))
        total2 += to_ord_set(intersection)

        i += 3

    answer1 = total1
    answer2 = total2

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
