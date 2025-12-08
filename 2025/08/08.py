import sys
import math
import re
from itertools import combinations

EXAMPLE_INPUT = """
""".strip()


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                self.parent[root_i] = root_j
                self.size[root_j] += self.size[root_i]
            else:
                self.parent[root_j] = root_i
                self.size[root_i] += self.size[root_j]

            return True

        return False

    def sizes(self):
        component_sizes = []
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                component_sizes.append(self.size[i])

        return sorted(component_sizes, reverse=True)


def dist(a, b):

    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2))


def main():
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))
    numbers_per_line = [[int(n) for n in re.findall(r"-?\d+", line)] for line in lines]

    # Part 1 and 2
    boxes = [tuple(box) for box in numbers_per_line]
    dsu = DisjointSet(len(boxes))

    dists = {}
    for b1, b2 in combinations(boxes, 2):
        if b1 == b2 or dists.get((b2, b1)):
            continue

        dists[(b1, b2)] = dist(b1, b2)

    i = 0
    for (b1, b2), _ in sorted(dists.items(), key=lambda item: item[1]):
        if i == 1000:
            answer1 = math.prod(dsu.sizes()[:3])
        i += 1

        i1 = boxes.index(b1)
        i2 = boxes.index(b2)

        if dsu.find(i1) == dsu.find(i2):
            continue
        else:
            dsu.union(i1, i2)

        if len(dsu.sizes()) == 1:
            answer2 = b1[0] * b2[0]
            break

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
