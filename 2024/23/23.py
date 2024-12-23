import sys

EXAMPLE_DATA = """
""".strip()


def edges_for_node(node, edges):
    result = []

    for edge in edges:
        if node not in edge:
            continue

        (x, y) = edge
        (x, y) = (y, x) if y == node else (x, y)

        result.append((x, y))

    return result


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))

    edges = []
    nodes = set()
    for line in lines:
        x = tuple(line.split("-"))
        edges.append(x)
        nodes.update(x)

    triplets = set()
    for e1, e2 in edges:
        for x, y in edges_for_node(e2, edges):
            de = x if x != e2 else y

            if de == e1:
                continue

            if (e1, de) in edges or (de, e1) in edges:
                triplet = tuple(sorted([e1, e2, de]))
                triplets.add(triplet)

    for triplet in triplets:
        for t in triplet:
            if t.startswith("t"):
                answer1 += 1
                break

    # Part 2
    groups = []
    for node in nodes:
        groups.append({node})

    for group in groups:
        for node in nodes:
            if all(
                ((node, group_node) in edges or (group_node, node) in edges)
                for group_node in group
            ):
                group.add(node)

    largest = {}
    for group in groups:
        if len(group) > len(largest):
            largest = group

    answer2 = ",".join(sorted(list(largest)))

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
