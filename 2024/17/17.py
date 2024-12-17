import sys
import re

EXAMPLE_DATA = """
""".strip()

A = B = C = IP = -1

ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7


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
    global A, B, C, IP
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
    global A, B, C, IP
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    chunks = list(filter(None, data.split("\n\n")))
    regs = list(filter(None, chunks[0].split("\n")))
    nums = [[int(l) for l in re.findall(r"-?\d+", reg)] for reg in regs]
    nums = [num for [num] in nums]

    A, B, C = nums
    IP = 0
    program = list(map(int, re.findall(r"-?\d+", chunks[1])))

    # Part 1
    output = run(program)
    answer1 = ",".join([str(x) for x in output])

    # Part 2
    output = []
    a = 0
    n = 1
    while output != program:
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
