import re


cycles = 0
reg = 1
sum = 0
draw_index = 0


def check_cycle():
    global sum
    global reg
    global cycles
    global draw_index

    if (cycles - 20) % 40 == 0:
        sum += cycles * reg

    if draw_index == reg or draw_index == reg - 1 or draw_index == reg + 1:
        print("#", end="")
    else:
        print(".", end="")

    draw_index += 1

    if cycles % 40 == 0:
        draw_index = 0
        print()


def main():
    global cycles
    global sum
    global reg

    answer1 = None
    answer2 = None

    file = open("./10.txt")
    data = file.read()
    lines = list(filter(None, data.split("\n")))

    for line in lines:
        match line.split():
            case ["noop"]:
                cycles += 1
                check_cycle()
            case ["addx", x]:
                for i in range(2):
                    cycles += 1
                    check_cycle()
                reg += int(x)

    answer1 = sum
    answer2 = "Printed..."

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
