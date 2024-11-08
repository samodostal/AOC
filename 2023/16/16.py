import sys

EXAMPLE_DATA = """
""".strip()


def reflect_speed(reflection, speed):
    reflected_speed = ()

    match speed:
        case (0, 1):  # Right
            reflected_speed = (-1, 0) if reflection == "/" else (1, 0)
        case (0, -1):  # Left
            reflected_speed = (1, 0) if reflection == "/" else (-1, 0)
        case (1, 0):  # Down
            reflected_speed = (0, -1) if reflection == "/" else (0, 1)
        case (-1, 0):  # Up
            reflected_speed = (0, 1) if reflection == "/" else (0, -1)
        case _:
            assert False

    return reflected_speed


def split_speeds(splitter, speed):
    split_speeds = []

    match speed:
        case (0, 1):  # Right
            split_speeds = [(1, 0), (-1, 0)] if splitter == "|" else [speed]
        case (0, -1):  # Left
            split_speeds = [(-1, 0), (1, 0)] if splitter == "|" else [speed]
        case (1, 0):  # Down
            split_speeds = [(0, -1), (0, 1)] if splitter == "-" else [speed]
        case (-1, 0):  # Up
            split_speeds = [(0, 1), (0, -1)] if splitter == "-" else [speed]
        case _:
            assert False

    return split_speeds


def simulate_beam(beam, map):
    pos_row, pos_col, speed_row, speed_col = beam

    next_beams = []
    tile = map[pos_row][pos_col]

    match tile:
        case ".":
            next_beams.append(
                (pos_row + speed_row, pos_col + speed_col, speed_row, speed_col)
            )
        case "/" | "L":
            reflected_speed_row, reflected_speed_col = reflect_speed(
                tile, (speed_row, speed_col)
            )
            next_beams.append(
                (
                    pos_row + reflected_speed_row,
                    pos_col + reflected_speed_col,
                    reflected_speed_row,
                    reflected_speed_col,
                )
            )
        case "|" | "-":
            speeds = split_speeds(tile, (speed_row, speed_col))
            for split_speed in speeds:
                next_beams.append(
                    (
                        pos_row + split_speed[0],
                        pos_col + split_speed[1],
                        split_speed[0],
                        split_speed[1],
                    )
                )

        case _:
            assert False

    return next_beams


def main():
    answer1 = 0
    answer2 = 0

    instruction = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, instruction.split("\n")))

    # (pos_row, pos_col, speed_row, speed_col)
    beams = [(0, 0, 0, 1)]
    visited = []

    while beams:
        beam = beams.pop(0)

        if beam in visited:
            continue

        next_beams = simulate_beam(beam, lines)

        for next_beam in next_beams:
            next_row, next_col, _, _ = next_beam
            if (
                next_row < 0
                or next_row >= len(lines)
                or next_col < 0
                or next_col >= len(lines[0])
            ):
                continue

            beams.append(next_beam)

        visited.append(beam)

    visited_positions = [(pos_row, pos_col) for pos_row, pos_col, _, _ in visited]
    answer1 = len(set(visited_positions))

    for speed in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        print("On speed: " + str(speed))
        all_beams = []
        if speed == (0, 1):
            all_beams = [
                (row, 0, speed[0], speed[1]) for row in range(len(lines))
            ]
        elif speed == (0, -1):
            all_beams = [
                (row, len(lines[0]) - 1, speed[0], speed[1])
                for row in range(len(lines))
            ]
        elif speed == (1, 0):
            all_beams = [
                (0, col, speed[0], speed[1]) for col in range(len(lines[0]))
            ]
        elif speed == (-1, 0):
            all_beams = [
                (len(lines) - 1, col, speed[0], speed[1])
                for col in range(len(lines[0]))
            ]

        for beam in all_beams:
            beams = [beam]
            visited = []
            while beams:
                beam = beams.pop(0)

                if beam in visited:
                    continue

                next_beams = simulate_beam(beam, lines)

                for next_beam in next_beams:
                    next_row, next_col, _, _ = next_beam
                    if (
                        next_row < 0
                        or next_row >= len(lines)
                        or next_col < 0
                        or next_col >= len(lines[0])
                    ):
                        continue

                    beams.append(next_beam)

                visited.append(beam)

            visited_positions = [(pos_row, pos_col) for pos_row, pos_col, _, _ in visited]
            visited_count = len(set(visited_positions))
            if visited_count > answer2:
                answer2 = visited_count

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
