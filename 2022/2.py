def main():
    answer1 = None
    answer2 = None

    file = open("./2.txt")
    data = file.read()
    lines = data.split("\n")

    points1 = 0
    points2 = 0

    # A, X = Rock //1
    # B, Y = Paper //2
    # C, Z = Scissors //3

    # X = lose
    # Y = draw
    # Z = win

    for line in lines:
        words = line.split()
        if not words:
            continue

        if words[1] == "X":
            points1 += 1
        elif words[1] == "Y":
            points1 += 2
        elif words[1] == "Z":
            points1 += 3

        if words[0] == "A":
            if words[1] == "X":
                points1 += 3
                points2 += 0 + 3
            elif words[1] == "Y":
                points1 += 6
                points2 += 3 + 1
            elif words[1] == "Z":
                points2 += 6 + 2
        elif words[0] == "B":
            if words[1] == "X":
                points2 += 0 + 1
            elif words[1] == "Y":
                points1 += 3
                points2 += 3 + 2
            elif words[1] == "Z":
                points1 += 6
                points2 += 6 + 3
        elif words[0] == "C":
            if words[1] == "X":
                points1 += 6
                points2 += 0 + 2
            elif words[1] == "Y":
                points2 += 3 + 3
            elif words[1] == "Z":
                points1 += 3
                points2 += 6 + 1

    answer1 = points1
    answer2 = points2

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
