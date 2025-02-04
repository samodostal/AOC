import sys
import re

EXAMPLE_INPUT = """
""".strip()


def calculate(wires, rules):
    q = rules.copy()
    w = wires.copy()

    while q:
        rule = q.pop(0)
        w1_in, gate, w2_in, w_out = rule

        if w.get(w1_in, None) is None or w.get(w2_in, None) is None:
            q.append(rule)
            continue

        out = None
        if gate == "AND":
            out = w[w1_in] & w[w2_in]
        elif gate == "OR":
            out = w[w1_in] | w[w2_in]
        elif gate == "XOR":
            out = w[w1_in] ^ w[w2_in]
        else:
            assert False

        w[w_out] = out

    result = 0
    x = 1
    for wire in sorted(w.keys()):
        if wire.startswith("z"):
            result += x if w[wire] else 0
            x *= 2

    return result


def wire_name_from_index(family, index):
    return f"{family}{index:02}"


def set_wires(x, y, wires):
    mask = 1
    index = 0

    x_name = "x00"
    y_name = "x00"

    while wires.get(x_name, None) != None and wires.get(y_name, None) != None:
        wires[x_name] = 1 if x & mask else 0
        wires[y_name] = 1 if y & mask else 0

        index += 1
        mask <<= 1
        x_name = wire_name_from_index("x", index)
        y_name = wire_name_from_index("y", index)


def generate_graph(rules, highlight_nodes):
    with open("graph.dot", "w") as f:
        f.write("digraph G {")

        for w1, _, w2, wo in rules:
            f.write(f"{w1} -> {wo};")
            f.write(f"{w2} -> {wo};")

        for n in highlight_nodes:
            f.write(f"{n} [style=filled, fillcolor=red];")

        f.write("}")


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    chunks = list(filter(None, input.split("\n\n")))
    wires = {
        w: int(v)
        for w, v in (re.split(r": |;", y) for y in filter(None, chunks[0].split("\n")))
    }
    rules = [
        (w1, g, w2, wo)
        for (w1, g, w2, _, wo) in [
            x.split() for x in filter(None, chunks[1].split("\n"))
        ]
    ]

    # Part 1
    answer1 = calculate(wires, rules)

    # Part 2
    broken_bits = set()

    SIMULATION = 1000
    BITSIZE = 44
    mask = 1
    for _ in range(SIMULATION):
        x, y = mask, mask
        set_wires(x, y, wires)
        calc_z = calculate(wires, rules)
        correct_z = x + y

        for i in range(BITSIZE + 1):
            calc_bit = 1 if calc_z & 1 << i else 0
            correct_bit = 1 if correct_z & 1 << i else 0

            if calc_bit != correct_bit:
                broken_bits.add(wire_name_from_index("z", i))

        mask <<= 1

    mismatches_filtered = set()
    for w1, _, w2, wo in rules:
        if wo in broken_bits:
            if not w1.startswith("x") or not w2.startswith("y"):
                mismatches_filtered.add(wo)

    # Broken bits: {'34', '10', '31', '21', '35', '09', '30', '20'}
    # broken around 09-10, 20-21, 30-31, 34-35

    # manual inspection around these places with generated graph

    # found swaps: z09 - nnf (around 09-10)
    # found swaps: z20 - nhs (around 20-21)
    # found swaps: ddn - kqh (around 30-31)
    # found swaps: wrc - z34 (around 34-35)

    found_nodes = ["z09", "nnf", "z20", "nhs", "ddn", "kqh", "wrc", "z34"]
    generate_graph(rules, found_nodes)

    answer2 = ",".join(sorted(found_nodes))

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
