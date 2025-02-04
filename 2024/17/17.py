import sys
import re

EXAMPLE_INPUT = """
""".strip()

A = B = C = -1

ADV, BXL, BST, JNZ, BXC, OUT, BDV, CDV = range(0, 8)


def combo(operand):
    global A, B, C
    return {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: A,
        5: B,
        6: C,
        7: -1,
    }[operand]


def run(program):
    global A, B, C
    IP = 0
    output = []

    while IP < len(program) - 1:
        instruction, operand = program[IP], program[IP + 1]
        combo_operand = combo(operand)

        IP += 2

        if instruction == ADV:
            A = A // (2**combo_operand)

        if instruction == BXL:
            B = B ^ operand

        if instruction == BST:
            B = combo(operand) % 8

        if instruction == JNZ:
            if A != 0:
                IP = operand

        if instruction == BXC:
            B = B ^ C

        if instruction == OUT:
            output.append(combo_operand % 8)

        if instruction == BDV:
            B = A // (2**combo_operand)

        if instruction == CDV:
            C = A // (2**combo_operand)

    return output


def main():
    global A, B, C
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    chunks = list(filter(None, input.split("\n\n")))

    A, B, C = list(map(int, re.findall(r"-?\d+", chunks[0])))
    program = list(map(int, re.findall(r"-?\d+", chunks[1])))

    # Part 1
    answer1 = ",".join([str(x) for x in run(program)])

    # Part 2
    output = []
    a = 0
    n = 1
    while n - 1 != len(program):
        while output[-n:] != program[-n:]:
            A = a
            output = run(program)
            a += 1

        a -= 1
        a *= 8
        n += 1

    answer2 = a // 8

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
