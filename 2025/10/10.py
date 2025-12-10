import sys
import re
from collections import deque
import z3

EXAMPLE_INPUT = """
""".strip()


def solve_diagram_bfs(target, schematics):
    target_mask = 0
    for i, ch in enumerate(target):
        if ch == "#":
            target_mask |= 1 << i

    schematic_masks = []
    for s in schematics:
        mask = 0
        for i in s:
            mask |= 1 << i

        schematic_masks.append(mask)

    queue = deque([(0, 0)])
    visited = {0}

    while queue:
        current, presses = queue.popleft()

        if current == target_mask:
            return presses

        for sm in schematic_masks:
            new_state = current ^ sm
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))

    return 0


def solve_joltics_z3(target, schematics):
    schematics_adder = []
    z3_vars = []
    solver = z3.Optimize()

    for i, s in enumerate(schematics):
        schematics_adder.append([0 for _ in target])

        v = z3.Int(f"v{i}")
        z3_vars.append(v)
        solver.add(v >= 0)

        for j in s:
            if j < len(target):
                schematics_adder[-1][j] = 1

    for i in range(len(target)):
        target_value = target[i]

        used_vars = []
        for j, s in enumerate(schematics_adder):
            add = s[i]
            if add:
                used_vars.append(z3_vars[j])

        sum_of_terms = z3.Sum(used_vars)
        solver.add(target_value == sum_of_terms)

    total_presses = z3.Sum(z3_vars)
    solver.minimize(total_presses)

    solver.check()
    model = solver.model()
    return model.evaluate(total_presses).as_long()


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))
    splits_per_line = [line.split() for line in lines]

    for splits in splits_per_line:
        diagram = splits[0][1:-1]
        schematics = [
            [int(n) for n in re.findall(r"-?\d+", line)] for line in splits[1:-1]
        ]
        joltics = [int(n) for n in re.findall(r"-?\d+", splits[-1])]

        answer1 += solve_diagram_bfs(diagram, schematics)
        answer2 += solve_joltics_z3(joltics, schematics)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
