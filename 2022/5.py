import re


def main():
    answer1 = None
    answer2 = None

    file = open("./5.txt")
    data = file.read()
    chunks = list(filter(None, data.split("\n\n")))

    crates = []
    instructions = []

    initial = True
    index = 0

    for line in chunks[0].split("\n"):
        for i in range(0, len(line), 4):
            if line[i + 1].isdecimal():
                break

            if line[i + 1]:
                if initial:
                    crates.append([])
            if line[i + 1] != " ":
                crates[index].insert(0, line[i + 1])
            index += 1
        index = 0
        initial = False

    for line in chunks[1].split("\n"):
        if not line:
            continue
        nums = list(map(int, re.findall(r"\d+", line)))
        instructions.append(nums)

    crates2 = [x[:] for x in crates]
    instructions2 = [x[:] for x in instructions]

    # part 1
    for instruction in instructions:
        count = instruction[0]
        crate_from = crates[instruction[1] - 1]

        popped = []
        for _ in range(count):
            popped.append(crate_from.pop())

        crates[instruction[2] - 1] = crates[instruction[2] - 1] + popped

    # part 2
    for instruction in instructions2:
        count = instruction[0]
        crate_from = crates2[instruction[1] - 1]

        popped = []
        for _ in range(count):
            popped.append(crate_from.pop())

        popped.reverse()

        crates2[instruction[2] - 1] = crates2[instruction[2] - 1] + popped

    answer1 = "".join([c[-1] for c in crates])
    answer2 = "".join([c[-1] for c in crates2])

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
