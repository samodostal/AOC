import sys
import re
import copy

EXAMPLE_DATA = """
""".strip()

char_to_index = {"x": 0, "m": 1, "a": 2, "s": 3}


def count_accepted_ranges(ranges, instructions, current):
    if current == "A":
        result = 1
        for r in [end - start for [start, end] in ranges]:
            assert r > 0
            result *= r
        return result

    if current == "R":
        return 0

    total_sum = 0

    ranges_left = copy.deepcopy(ranges)

    for step in instructions[current]:
        is_simple = step[0] is None

        if is_simple:
            total_sum += count_accepted_ranges(ranges_left, instructions, step[3])
        else:
            [var, cmp, num, dst] = step

            corresponding_ranges = copy.deepcopy(ranges_left)
            new_ranges_left = copy.deepcopy(ranges_left)

            corresponding_ranges[char_to_index[var]][1 if cmp == "<" else 0] = (
                num if cmp == "<" else num + 1
            )
            new_ranges_left[char_to_index[var]][0 if cmp == "<" else 1] = (
                num if cmp == "<" else num + 1
            )

            is_valid = True
            for rng in corresponding_ranges:
                if rng[0] >= rng[1]:
                    is_valid = False
                    break

            if not is_valid:
                continue

            total_sum += count_accepted_ranges(corresponding_ranges, instructions, dst)
            ranges_left = new_ranges_left

    return total_sum


def is_test_accepted(test, instructions, entry_instruction_name):
    destination = None

    instruction = instructions[entry_instruction_name]
    for part in instruction:
        [var, cmp, num, dst] = part
        is_simple = part[0] is None
        if is_simple:
            destination = part[3]
            break

        if cmp == ">":
            if test[char_to_index[var]] > num:
                destination = dst
                break
        else:
            if test[char_to_index[var]] < num:
                destination = dst
                break

    if destination == "A":
        return True

    if destination == "R":
        return False

    return is_test_accepted(test, instructions, destination)


def main():
    answer1 = 0
    answer2 = 0

    tests_data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    chunks = list(filter(None, tests_data.split("\n\n")))

    [instructions_data, tests_data] = chunks
    instructions = {}

    for instruction in list(filter(None, instructions_data.split("\n"))):
        name, steps = instruction.split("{")

        steps = steps[:-1]

        instructions_for_line = []

        for step in steps.split(","):
            # variable, comparison, number, destination
            instr = (None, None, None, None)

            is_simple_step = ":" not in step
            if is_simple_step:
                instr = (None, None, None, step)
            else:
                var, num, dst = re.split(">|<|:", step)
                cmp = ">" if ">" in step else "<"

                instr = (var, cmp, int(num), dst)

            instructions_for_line.append(instr)

        instructions[name] = instructions_for_line

    tests = []

    for line in list(filter(None, tests_data.split("\n"))):
        nums = re.findall(r"-?\d+", line)
        tests.append([int(i) for i in nums])

    for t in tests:
        is_accepted = is_test_accepted(t, instructions, "in")
        if is_accepted:
            answer1 += sum(t)

    # Part 2
    ranges = [[1, 4001] for _ in range(4)]
    answer2 = count_accepted_ranges(ranges, instructions, "in")

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
