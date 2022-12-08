import re

UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3

DIR_ADDERS = [[0, -1], [1, 0], [-1, 0], [0, 1]]


def check_direction(x, y, map):
    if x == 0 or x == len(map[y]) - 1 or y == 0 or y == len(map) - 1:
        return True

    value = map[y][x]

    for dir in range(UP, DOWN + 1):
        new_x = x
        new_y = y
        while True:
            new_x += DIR_ADDERS[dir][0]
            new_y += DIR_ADDERS[dir][1]

            if map[new_y][new_x] >= value:
                break
            if (
                new_x <= 0
                or new_y <= 0
                or new_x >= len(map[0]) - 1
                or new_y >= len(map) - 1
            ):
                return True

    return False


def scenic_score(x, y, map):
    score = 1

    value = map[y][x]

    for dir in range(UP, DOWN + 1):
        new_x = x
        new_y = y
        cur_scenic = 0
        while True:
            new_x += DIR_ADDERS[dir][0]
            new_y += DIR_ADDERS[dir][1]

            cur_scenic += 1

            if (
                new_x <= 0
                or new_y <= 0
                or new_x >= len(map[0]) - 1
                or new_y >= len(map) - 1
            ):
                break

            if map[new_y][new_x] >= value:
                break
        score *= cur_scenic

    return score


def main():
    answer1 = None
    answer2 = None

    file = open("./8.txt")
    data = file.read()
    lines = list(filter(None, data.split("\n")))
    lines_nums = [list(map(int, re.findall(r"\d{1}", l))) for l in lines]

    dirs_count = 0
    max_score = 0

    for y in range(len(lines_nums)):
        row = lines_nums[y]
        for x in range(len(row)):
            max_score = max(max_score, scenic_score(x, y, lines_nums))
            if check_direction(x, y, lines_nums):
                dirs_count += 1

    answer1 = dirs_count
    answer2 = max_score

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
