import sys
import re
from collections import defaultdict
import heapq

EXAMPLE_DATA = """
""".strip()

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# L, H, N = 0, 6, 12
L, H, N = 0, 70, 1024


def dijkstra(graph, start):
    dists = {node: float("inf") for node in graph}
    dists[start] = 0

    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)

        if d > dists[node]:
            continue

        for neigh in graph[node]:
            nd = d + 1

            if nd < dists[neigh]:
                dists[neigh] = nd
                heapq.heappush(pq, (nd, neigh))

    return dists


def create_grid(sliced_nums):
    D = defaultdict(lambda: "X")
    for x in range(0, H + 1):
        for y in range(0, H + 1):
            D[(x, y)] = "#" if [x, y] in sliced_nums else "."

    return D


def create_graph(D):
    G = {}
    for x in range(0, H + 1):
        for y in range(0, H + 1):
            if D[(x, y)] == "#":
                continue

            G[(x, y)] = []
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx > H or ny < 0 or ny > H:
                    continue

                if D[(nx, ny)] == ".":
                    G[(x, y)].append((nx, ny))
    return G


def path_exists_for_nums(sliced_nums, D, G):
    D = create_grid((sliced_nums))
    G = create_graph(D)

    distances = dijkstra(G, (0, 0))

    return distances[(H, H)] != float("inf")


def main():
    global N
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )
    lines = list(filter(None, data.split("\n")))
    nums = [[int(n) for n in re.findall(r"-?\d+", line)] for line in lines]
    sliced_nums = nums[:N]

    # Part 1
    D = create_grid(sliced_nums)
    G = create_graph(D)

    answer1 = dijkstra(G, (0, 0))[(H, H)]

    # Part 2
    left, right = N, len(nums)
    while left <= right:
        mid = (left + right) // 2
        sliced_nums = nums[:mid]

        if path_exists_for_nums(sliced_nums, D, G):
            left = mid + 1
        else:
            right = mid - 1

    [x, y] = nums[left - 1]
    answer2 = str(x) + ", " + str(y)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
