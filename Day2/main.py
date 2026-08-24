import time
import utils
import re

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

    invalid = []
    num_ranges = data.split(",")
    for num_range in num_ranges:
        first, last = num_range.split("-")
        first = int(first)
        last = int(last)
        for i in range(first, last+1):
            match = re.fullmatch(r"(.+)\1", str(i))
            if match:
                invalid.append(i)

    return sum(invalid)


def part2(data):
    invalid = []
    num_ranges = data.split(",")
    for num_range in num_ranges:
        first, last = num_range.split("-")
        first = int(first)
        last = int(last)
        for i in range(first, last+1):
            match = re.fullmatch(r"(.+)\1+", str(i))
            if match:
                invalid.append(i)

    return sum(invalid)


if __name__ == "__main__":
    main()