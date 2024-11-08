import sys
import networkx as nx
import matplotlib.pyplot as plt

EXAMPLE_DATA = """

jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr

""".strip()


def main():
    answer1 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    dict = {}

    for line in lines:
        key, values = line.split(": ")
        values = values.split()

        dict[key] = set(values)
        for value in values:
            if dict.get(value) is None:
                dict[value] = set()
            dict[value].add(key)

    drawable_graph = nx.Graph()

    for node, edges in dict.items():
        for edge in edges:
            drawable_graph.add_edge(node.upper(), edge.upper())

    # Which edges to remove chosen from image
    # plt.figure()
    # nx.draw(drawable_graph, with_labels=True)
    # plt.show()

    found_edges = []
    node_part_of_group = "x"
    if len(sys.argv) > 2:
        found_edges = [("ldl", "fpg"), ("nxk", "dfk"), ("hcf", "lhn")]
        node_part_of_group = "qxb"
    else:
        found_edges = [("nvd", "jqt"), ("hfx", "pzl"), ("bvb", "cmg")]
        node_part_of_group = "cmg"

    size = 7

    visited = set()
    queue = [node_part_of_group]
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue

        visited.add(node)
        size += 1

        for edge in dict[node]:
            if (node, edge) in found_edges or (edge, node) in found_edges:
                continue

            queue.append(edge)

    answer1 = size * (len(dict) - size)

    print("Answer 1: ", answer1)


if __name__ == "__main__":
    main()
