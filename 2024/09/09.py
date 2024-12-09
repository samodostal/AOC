import sys

EXAMPLE_DATA = """
""".strip()


def find_next_empty(i, x):
    for j in range(i + 1, len(x)):
        if x[j] == ".":
            return j

    return -1


def find_empty_range(range_size, x):
    s = 0
    for i in range(0, len(x)):
        if x[i] == ".":
            s += 1
        else:
            s = 0

        if s == range_size:
            return (i - range_size + 1, i)

    return (-1, -1)


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    input = list(filter(None, data.split("\n")))[0]

    x1 = []
    id = 0
    for i, num in enumerate(input):
        for _ in range(int(num)):
            x1.append(id if i % 2 == 0 else ".")

        if i % 2 == 0:
            id += 1

    x = x1.copy()

    # Part 1
    first_empty = find_next_empty(0, x1)

    for i in range(len(x1) - 1, 0, -1):
        if i <= first_empty:
            break

        num = x1[i]
        if num == ".":
            continue

        x1[first_empty] = num
        x1[i] = "."

        first_empty = find_next_empty(first_empty, x1)

    for i, num in enumerate(x1):
        if num != ".":
            answer1 += i * num

    # Part 2
    fx, fy = -1, -1
    curr = -1

    for i in range(len(x) - 1, 0, -1):
        if x[i] != ".":
            fy = i
            curr = x[i]
            break

    for i in range(len(x) - 1, 0, -1):
        if x[i] == curr:
            continue

        fx = i + 1
        if curr != ".":
            (nx, ny) = find_empty_range(fy - fx + 1, x)
            if nx != -1 and ny <= fx:
                for j in range(nx, ny + 1):
                    x[j] = curr
                for j in range(fx, fy + 1):
                    x[j] = "."

        curr = x[i]
        fy = i

    for i, num in enumerate(x):
        if num != ".":
            answer2 += i * num

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
