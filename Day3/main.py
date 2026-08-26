import time
import utils
from collections import Counter


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

    joltages = []
    for line in data:
        largest = 0
        line=line.strip()
        for a in range(len(line)):
            for b in range(a+1, len(line)):
                value = int(line[a]+line[b])
                if value > largest:
                    largest = value
        joltages.append(largest)
    return sum(joltages)


def part2(data):
    joltages = []
    for line in data:
        line = line.strip()
        total_length = len(line)
        largest = []
        for i, num in enumerate(line):
            if i == 0:
                largest.append(num)
            else:
                if int(num) > int(largest[0]) and i <= total_length - 12:
                    largest = [num]
                elif len(largest) > 1 and i <= total_length - 11 and int(num) > int(largest[1]):
                    largest = list(largest[0]) + [num]
                elif len(largest) > 2 and i <= total_length - 10 and int(num) > int(largest[2]):
                    largest = largest[0:2] + [num]    
                elif len(largest) > 3 and i <= total_length - 9 and int(num) > int(largest[3]):
                    largest = largest[0:3] + [num]
                elif len(largest) > 4 and i <= total_length - 8 and int(num) > int(largest[4]):
                    largest = largest[0:4] + [num]
                elif len(largest) > 5 and i <= total_length - 7 and int(num) > int(largest[5]):
                    largest = largest[0:5] + [num]
                elif len(largest) > 6 and i <= total_length - 6 and int(num) > int(largest[6]):
                    largest = largest[0:6] + [num]
                elif len(largest) > 7 and i <= total_length - 5 and int(num) > int(largest[7]):
                    largest = largest[0:7] + [num]
                elif len(largest) > 8 and i <= total_length - 4 and int(num) > int(largest[8]):
                    largest = largest[0:8] + [num]
                elif len(largest) > 9 and i <= total_length - 3 and int(num) > int(largest[9]):
                    largest = largest[0:9] + [num]
                elif len(largest) > 10 and i <= total_length - 2 and int(num) > int(largest[10]):
                    largest = largest[0:10] + [num]
                elif len(largest) > 11 and i <= total_length - 1 and int(num) > int(largest[11]):
                    largest = largest[0:11] + [num]
                elif len(largest) < 12:
                    largest.append(num)
        joltages.append(int("".join(largest)))

    return sum(joltages)

if __name__ == "__main__":
    main()