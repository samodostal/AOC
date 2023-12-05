import sys

EXAMPLE_DATA = """
""".strip()


def fill_dict(chunk):
    lines = list(filter(None, chunk.split("\n")))
    lines.pop(0)

    out = []
    for line in lines:
        out.append([int(i) for i in line.split()])

    return out


def use_dict(num, dict):
    for [destination_start, source_start, range_length] in dict:
        if num >= source_start and num < source_start + range_length:
            diff = num - source_start
            return destination_start + diff

    return num


def find_overlap(r1_start, r1_end, r2_start, r2_end):
    overlap_start = max(r1_start, r2_start)
    overlap_end = min(r1_end, r2_end)

    if overlap_start < overlap_end:
        not_overlapped = []

        if r1_start < overlap_start:
            not_overlapped.append([r1_start, overlap_start])

        if overlap_end < r1_end:
            not_overlapped.append([overlap_end, r1_end])

        return ([overlap_start, overlap_end], not_overlapped)
    else:
        return (None, [[r1_start, r1_end]])


def use_dict_ranges(ranges, dict):
    output_ranges = []
    for r in ranges:
        unprocessed_ranges = [r]
        while unprocessed_ranges:
            [min, max] = unprocessed_ranges.pop(0)

            found_overlap = False

            for [destination_start, source_start, range_length] in dict:
                source_end = source_start + range_length  # non inclusive
                overlap, remainder = find_overlap(min, max, source_start, source_end)

                if not overlap:
                    continue

                found_overlap = True

                diff1 = overlap[0] - source_start
                diff2 = overlap[1] - source_start
                output_ranges.append(
                    [destination_start + diff1, destination_start + diff2]
                )

                for r in remainder:
                    unprocessed_ranges.append(r)

                break

            if not found_overlap:
                output_ranges.append([min, max])
                break

    return output_ranges


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    chunks = list(filter(None, data.split("\n\n")))

    seeds = [int(i) for i in chunks[0].split(": ")[1].split()]

    seed_ranges = []

    for i in range(0, len(seeds), 2):
        s1 = seeds[i]
        s2 = seeds[i + 1]
        seed_ranges.append([s1, s1 + s2])

    seed_to_soil = fill_dict(chunks[1])
    soil_to_fertilizer = fill_dict(chunks[2])
    fertilizer_to_water = fill_dict(chunks[3])
    water_to_light = fill_dict(chunks[4])
    light_to_temperature = fill_dict(chunks[5])
    temperature_to_humidity = fill_dict(chunks[6])
    humidity_to_location = fill_dict(chunks[7])

    # Part 1
    locations = []
    for seed in seeds:
        soil = use_dict(seed, seed_to_soil)
        fertilizer = use_dict(soil, soil_to_fertilizer)
        water = use_dict(fertilizer, fertilizer_to_water)
        light = use_dict(water, water_to_light)
        temperature = use_dict(light, light_to_temperature)
        humidity = use_dict(temperature, temperature_to_humidity)
        location = use_dict(humidity, humidity_to_location)

        locations.append(location)

    answer1 = min(locations)

    # Part 2
    soil_ranges = use_dict_ranges(seed_ranges, seed_to_soil)
    fertilizer_ranges = use_dict_ranges(soil_ranges, soil_to_fertilizer)
    water_ranges = use_dict_ranges(fertilizer_ranges, fertilizer_to_water)
    light_ranges = use_dict_ranges(water_ranges, water_to_light)
    temperature_ranges = use_dict_ranges(light_ranges, light_to_temperature)
    humidity_ranges = use_dict_ranges(temperature_ranges, temperature_to_humidity)
    location_ranges = use_dict_ranges(humidity_ranges, humidity_to_location)

    answer2 = min(location_range[0] for location_range in location_ranges)

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
