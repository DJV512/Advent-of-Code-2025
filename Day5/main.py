import time
import utils


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(data)
    part2_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time):.2f} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time):.2f} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time):.2f} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time):.2f} ms")
    print("---------------------------------------------------")


output = True  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    # FILENAME = "sample_input.txt"
    FILENAME = "input.txt"
    
    return utils.parse_input(FILENAME, method="raw_read")


def part1(data):
    fresh = 0
    ranges, ids = data.split("\n\n")
    individual_ranges = ranges.split("\n")
    final_ranges = []
    for line in individual_ranges:
        final_ranges.append(tuple(line.strip().split("-")))

    final_ids = ids.split("\n")

    for id in final_ids:
        for final_range in final_ranges:
            if int(final_range[0]) <= int(id) <= int(final_range[1]):
                fresh += 1
                break
    return fresh


def part2(data):
    ranges, _ = data.split("\n\n")
    individual_ranges = ranges.split("\n")
    fresh_ids = []
    for line in individual_ranges:
        low, high = line.strip().split("-")
        fresh_ids.append([int(low), int(high)])

    final_fresh_ids = []
    correct = False

    while not correct:
        correct = True
        for new_low, new_high in fresh_ids:
            if len(final_fresh_ids) == 0:
                final_fresh_ids.append([new_low, new_high])
            else:
                for i, (low, high) in enumerate(final_fresh_ids):
                    changed = False
                    if low <= new_low <= high and low <= new_high <= high:
                        changed = True
                        correct = False
                        break
                    elif new_low < low and low <= new_high <= high:
                        changed = True
                        correct = False
                        final_fresh_ids[i][0] = new_low
                        break
                    elif new_low < low and new_high > high:
                        changed = True
                        correct = False
                        final_fresh_ids[i] = [new_low, new_high]
                        break
                    elif low <= new_low <= high and new_high > high:
                        changed = True
                        correct = False
                        final_fresh_ids[i][1] = new_high
                        break
                if not changed:
                    final_fresh_ids.append([new_low, new_high])

        fresh_ids = sorted(final_fresh_ids)
        final_fresh_ids = []

    fresh_count = 0
    for low, high in fresh_ids:
        fresh_in_range = high - low + 1
        fresh_count += fresh_in_range

    return fresh_count

if __name__ == "__main__":
    main()