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
    
    return utils.parse_input(FILENAME, method="raw_lines")


def part1(data):

    location = 50
    count = 0

    for line in data:
        direction = line[0]
        if direction == "L":
            location -= int(line[1:])
            while location < 0:
                location += 100
        else:
            location += int(line[1:])
            if location >= 100:
                location %= 100

        if location == 0:
            count += 1

    return count


def part2(data):

    location = 50
    count = 0

    for line in data:
        # print(f"Starting location = {location}, starting count = {count}, next rotation = {line.strip()}")
        direction = line[0]
        rotation = int(line[1:])
        full_rotations = rotation // 100
        remainder = rotation % 100
        count += full_rotations 
        if direction == "L":
            location -= remainder
            if location == 0:
                count += 1
            elif location < 0:
                location += 100
                if location + remainder != 100:
                    count += 1
        else:
            location += remainder
            if location == 0:
                count += 1
            elif location >= 100:
                location -= 100
                count += 1

        # print(f"Final location = {location}, count = {count}\n")

    return count


if __name__ == "__main__":
    main()