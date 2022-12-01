def main():
    answer1 = None
    answer2 = None

    file = open("./1.txt")
    data = file.read()
    chunks = data.split("\n\n")

    sums = sorted([sum(map(int, chunk.split())) for chunk in chunks])

    answer1 = sums[-1]
    answer2 = sum(sums[-3:])

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
