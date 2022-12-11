import re
from math import floor
from copy import deepcopy


def operate(num, operation):
    op = operation.copy()
    for i in range(len(op)):
        if op[i] == "old":
            op[i] = num

    match op:
        case [old1, "+", old2]:
            return int(old1) + int(old2)
        case [old1, "*", old2]:
            return int(old1) * int(old2)
        case [old1, _, old2]:
            assert False


def main():
    answer1 = None
    answer2 = None

    file = open("./11.txt")
    data = file.read()
    chunks = list(filter(None, data.split("\n\n")))

    items = []
    operations = []
    tests = []
    trues = []
    falses = []

    common_divisor = 1

    index = 0

    for chunk in chunks:
        lines = list(filter(None, chunk.split("\n")))
        op_string = lines[2].split("= ")[1]
        tests_val = list(map(int, re.findall(r"\d+", lines[3])))
        trues_val = list(map(int, re.findall(r"\d+", lines[4])))
        falses_val = list(map(int, re.findall(r"\d+", lines[5])))

        assert len(tests_val) == 1

        items.append(list(map(int, re.findall(r"\d+", lines[1]))))
        operations.append(op_string.split())
        tests.append(tests_val[0])
        trues.append(trues_val[0])
        falses.append(falses_val[0])
        common_divisor *= tests_val[0]
        index += 1

    assert (
        len(items)
        == len(operations)
        == len(tests)
        == len(trues)
        == len(falses)
    )

    inspections = [0 for _ in range(len(items))]

    inspections2 = deepcopy(inspections)
    items2 = deepcopy(items)
    operations2 = deepcopy(operations)
    tests2 = deepcopy(tests)
    trues2 = deepcopy(trues)
    falses2 = deepcopy(falses)

    # 1
    for x in range(20):
        for i in range(len(items)):
            for j, num in enumerate(items[i]):
                inspections[i] += 1
                calculated = operate(num, operations[i])

                calculated /= 3
                calculated = floor(calculated)

                if calculated % tests[i] == 0:
                    items[trues[i]].append(calculated)
                else:
                    items[falses[i]].append(calculated)

                items[i][j] = "X"
        items = [list(filter(lambda a: a != "X", x)) for x in items]

    # 2
    for x in range(10000):
        for i in range(len(items2)):
            for j, num in enumerate(items2[i]):
                inspections2[i] += 1
                calculated = operate(num, operations2[i])

                calculated %= common_divisor

                if calculated % tests2[i] == 0:
                    items2[trues2[i]].append(calculated)
                else:
                    items2[falses2[i]].append(calculated)

                items2[i][j] = "X"
        items2 = [list(filter(lambda a: a != "X", x)) for x in items2]

    inspections.sort()
    inspections2.sort()

    answer1 = inspections[-1] * inspections[-2]
    answer2 = inspections2[-1] * inspections2[-2]

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
