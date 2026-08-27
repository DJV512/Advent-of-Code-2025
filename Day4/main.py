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
    
    return utils.parse_input(FILENAME, method="grid_list")


def part1(data):

    y_len = len(data)
    x_len = len(data[0])

    accessible = 0
    for y in range(y_len):
        for x in range (x_len):
            count = 0
            if data[y][x] == "@":
                for (dir_y, dir_x) in utils.DIRS_8:
                    if 0 <= y + dir_y < y_len and 0 <= x + dir_x < x_len:
                        if data[y+dir_y][x+dir_x] == "@":
                            count += 1
                if count < 4:
                    accessible += 1

    return accessible


def part2(data):

    y_len = len(data)
    x_len = len(data[0])

    accessible = 0
    currently_removed = 1
    while currently_removed > 0:
        currently_removed = 0
        coords = []
        for y in range(y_len):
            for x in range (x_len):
                count = 0
                if data[y][x] == "@":
                    for (dir_y, dir_x) in utils.DIRS_8:
                        if 0 <= y + dir_y < y_len and 0 <= x + dir_x < x_len:
                            if data[y+dir_y][x+dir_x] == "@":
                                count += 1
                    if count < 4:
                        accessible += 1
                        currently_removed += 1
                        coords.append((y,x))
        for y,x in coords:
            data[y][x] = "."

    return accessible


if __name__ == "__main__":
    main()