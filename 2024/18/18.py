import sys
import re
import heapq

EXAMPLE_INPUT = """
""".strip()

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# H, N = 6, 12
H, N = 70, 1024


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


def create_graph(nums):
    G = {}
    for x in range(H + 1):
        for y in range(H + 1):
            if (x, y) in nums:
                continue

            G[(x, y)] = []
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx > H or ny < 0 or ny > H:
                    continue

                if (nx, ny) not in nums:
                    G[(x, y)].append((nx, ny))
    return G


def main():
    global N
    answer1 = 0
    answer2 = 0

    input = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--input"
        else EXAMPLE_INPUT
    )
    lines = list(filter(None, input.split("\n")))
    walls = [tuple(int(n) for n in re.findall(r"-?\d+", line)) for line in lines]
    walls_sliced = walls[:N]

    # Part 1
    answer1 = dijkstra(create_graph(walls_sliced), (0, 0))[(H, H)]

    # Part 2
    left, right = N, len(walls)
    while left <= right:
        mid = (left + right) // 2
        walls_sliced = walls[:mid]

        if dijkstra(create_graph(set(walls_sliced)), (0, 0))[(H, H)] != float("inf"):
            left = mid + 1
        else:
            right = mid - 1

    [x, y] = walls[left - 1]
    answer2 = str(x) + "," + str(y)

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
