import re


def main():
    answer1 = None
    answer2 = None

    file = open("./4.txt")
    data = file.read()
    lines = list(filter(None, data.split("\n")))

    nums = [list(map(int, re.findall(r"\d+", line))) for line in lines]

    count = 0
    count2 = 0

    for num in nums:
        if (num[0] >= num[2] and num[1] <= num[3]) or (
            num[0] <= num[2] and num[1] >= num[3]
        ):
            count += 1

        for x in range(num[0], num[1] + 1):
            if (
                x == num[2]
                or x == num[3]
                or (x >= num[2] and x <= num[3])
            ):
                count2 += 1
                break

    answer1 = count
    answer2 = count2

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
