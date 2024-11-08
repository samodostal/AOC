import sys
import re
import math

EXAMPLE_DATA = """

broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output

""".strip()

# % - Flip-flop, on/off, initially off
# high -> nothing
# low -> toggle on/off + send pulse high-for-on, low-for-off

# & - Conjunction module, remembers previous pulse
# low pulse by default
# on pulse -> remember, if all high pulses -> send low pulse, otherwise -> high pulse

# broadcaaster sends same pulse it receives


def toggle_pulse(pulse):
    return 0 if pulse == 1 else 1


def main():
    answer1 = 0
    answer2 = 0

    tests_data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, tests_data.split("\n")))

    broadcaster_destinations = []
    flip_flops = {}
    conjunction_modules = {}
    memory = {}

    for line in lines:
        source, destination = line.split(" -> ")

        if "broadcaster" in line:
            broadcaster_destinations = destination.split(", ")
            continue

        if "%" in line:
            flip_flops[source[1:]] = destination.split(", ")
            memory[source[1:]] = 0

        if "&" in line:
            conjunction_modules[source[1:]] = destination.split(", ")
            memory[source[1:]] = []

    for line in lines:
        source, destination = line.split(" -> ")

        for cm in conjunction_modules.keys():
            if cm in destination:
                memory[cm].append((source[1:], 0))

    cycles = 0
    high_pulses, low_pulses = 0, 0
    memory1 = memory.copy()

    while cycles < 1000:
        cycles += 1
        low_pulses += 1
        stack = [(str("broadcaster"), dest, 0) for dest in broadcaster_destinations]

        stack_trace = []

        while stack:
            instr = stack.pop(0)
            stack_trace.append(instr)

            source, destination, pulse = instr

            if pulse == 1:
                high_pulses += 1
            else:
                low_pulses += 1

            if destination == "output" or destination == "rx":
                continue

            is_flip_flop = destination in flip_flops.keys()

            if is_flip_flop:
                if pulse == 0:
                    memory1[destination] = toggle_pulse(memory1[destination])

                    for dest in flip_flops[destination]:
                        stack.append((destination, dest, memory1[destination]))
                else:
                    continue
            else:
                for i, cell in enumerate(memory1[destination]):
                    if cell[0] == source:
                        cell = (cell[0], pulse)
                        memory1[destination][i] = cell

                found_zero = False
                for cell in memory1[destination]:
                    if cell[1] == 0:
                        found_zero = True
                        for dest in conjunction_modules[destination]:
                            stack.append((destination, dest, 1))
                        break

                if not found_zero:
                    for dest in conjunction_modules[destination]:
                        stack.append((destination, dest, 0))

    answer1 = low_pulses * high_pulses

    # Part 2

    loops = [0 for _ in range(4)]
    cycles = 0

    while cycles < 5000:
        cycles += 1
        stack = [(str("broadcaster"), dest, 0) for dest in broadcaster_destinations]
        stack_trace = []

        while stack:
            instr = stack.pop(0)
            stack_trace.append(instr)
            
            for i, (_, val) in enumerate(memory["hj"]):
                if val == 1 and loops[i] == 0:
                    loops[i] = cycles

            source, destination, pulse = instr

            if destination == "output" or destination == "rx":
                continue

            is_flip_flop = destination in flip_flops.keys()

            if is_flip_flop:
                if pulse == 0:
                    memory[destination] = toggle_pulse(memory[destination])

                    for dest in flip_flops[destination]:
                        stack.append((destination, dest, memory[destination]))
                else:
                    continue
            else:
                for i, cell in enumerate(memory[destination]):
                    if cell[0] == source:
                        cell = (cell[0], pulse)
                        memory[destination][i] = cell

                found_zero = False
                for cell in memory[destination]:
                    if cell[1] == 0:
                        found_zero = True
                        for dest in conjunction_modules[destination]:
                            stack.append((destination, dest, 1))
                        break

                if not found_zero:
                    for dest in conjunction_modules[destination]:
                        stack.append((destination, dest, 0))

    answer2 = math.lcm(*loops)

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
