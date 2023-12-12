import sys

EXAMPLE_DATA = """
""".strip()


def counts_correspond_to_template_fully(template, counts):
    template_counts = []
    current_count = 0

    for ch in template:
        if ch == "#":
            current_count += 1
        elif current_count != 0:
            template_counts.append(current_count)
            current_count = 0

    if current_count != 0:
        template_counts.append(current_count)

    return template_counts == counts


def counts_correspond_to_template_partialy(template, counts):
    template_counts = []
    current_count = 0

    for ch in template:
        if ch == "#":
            current_count += 1
        elif current_count != 0:
            template_counts.append(current_count)
            current_count = 0

    if current_count != 0:
        template_counts.append(current_count)

    if max(template_counts, default=0) > max(counts, default=0):
        return False

    return True


def count_arrangements(template, counts, position, position_count, matched_count, memo):
    memo_key = (position, position_count, matched_count)
    if memo_key in memo:
        return memo[memo_key]

    return_value = 0

    if len(template) == position:
        if len(counts) == position_count:
            return_value = 1

    elif template[position] == "#":
        return_value = count_arrangements(
            template, counts, position + 1, position_count, matched_count + 1, memo
        )

    elif template[position] == "." or len(counts) == position_count:
        if position_count < len(counts) and matched_count == counts[position_count]:
            return_value = count_arrangements(
                template, counts, position + 1, position_count + 1, 0, memo
            )
        elif matched_count == 0:
            return_value = count_arrangements(
                template, counts, position + 1, position_count, 0, memo
            )
        else:
            return_value = 0

    else:
        hashes_found, dots_found = 0, 0

        hashes_found = count_arrangements(
            template, counts, position + 1, position_count, matched_count + 1, memo
        )

        if matched_count == 0:
            dots_found = count_arrangements(
                template, counts, position + 1, position_count, 0, memo
            )
        elif matched_count == counts[position_count]:
            dots_found = count_arrangements(
                template, counts, position + 1, position_count + 1, 0, memo
            )

        return_value = hashes_found + dots_found

    memo[memo_key] = return_value
    return return_value


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    data = []

    for line in lines:
        template, counts = line.split()
        a1 = count_arrangements(
            template + ".", [int(i) for i in counts.split(",")], 0, 0, 0, {}
        )
        answer1 += a1

        template_duplicated = (template + "?") * 4 + template + "."
        counts_duplicated = (counts + ",") * 4 + counts

        a2 = count_arrangements(
            template_duplicated,
            [int(i) for i in counts_duplicated.split(",")],
            0,
            0,
            0,
            {},
        )
        answer2 += a2

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
