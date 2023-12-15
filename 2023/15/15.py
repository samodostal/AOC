import sys

EXAMPLE_DATA = """
""".strip()


def main():
    answer1 = 0
    answer2 = 0

    instruction = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, instruction.split("\n")))

    # Part 1
    for instr in lines[0].split(","):
        hash = 0
        for char in instr:
            ascii_val = ord(char)
            hash += ascii_val
            hash *= 17
            hash %= 256
        answer1 += hash

    # Part 2
    boxes = {}
    for instruction in lines[0].split(","):
        lens = instruction.split("=")[0]
        is_op_equals = "=" in instruction
        new_value = instruction.split("=")[1] if is_op_equals else 0
        lens = lens[:-1] if not is_op_equals else lens

        hash = 0
        for char in lens:
            ascii_val = ord(char)
            hash += ascii_val
            hash *= 17
            hash %= 256

        if is_op_equals:
            if boxes.get(hash) is None:
                boxes[hash] = []

            for i, (box_lens, _) in enumerate(boxes[hash]):
                if lens == box_lens:
                    boxes[hash][i] = (box_lens, new_value)
                    break
            else:
                boxes[hash].append((lens, new_value))
        else:
            if boxes.get(hash) is None:
                continue

            new_box = []
            for box_lens, box_value in boxes[hash]:
                if lens == box_lens:
                    continue
                new_box.append((box_lens, box_value))

            if not new_box:
                del boxes[hash]
            else:
                boxes[hash] = new_box

    for key in boxes.keys():
        for i, (box_lens, box_value) in enumerate(boxes[key]):
            answer2 += (1 + key) * (1 + i) * int(box_value)

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
