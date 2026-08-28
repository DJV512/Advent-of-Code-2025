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

    one = data[0].strip().split()
    two = data[1].strip().split()
    three = data[2].strip().split()
    four = data[3].strip().split()
    op = data[4].strip().split()

    results = []
    for i in range(len(one)):
        if op[i] == "+":
            result = int(one[i]) + int(two[i]) + int(three[i]) + int(four[i])
            results.append(result)
        else:
            result = int(one[i]) * int(two[i]) * int(three[i]) * int(four[i])
            results.append(result)

    return sum(results)

              
def part2(data):

    list_one = data[0].strip()
    list_two = data[1].strip()
    list_three = data[2].strip()
    list_four = data[3].strip()
    list_op = data[4].strip() + " "

    transformed_nums = []
    for i in range(len(list_one)):

        one = list_one[i]
        two = list_two[i]
        three = list_three[i]
        four = list_four[i]
        five = list_op[i]

        if five != " ":
            transformed_nums.append(five)

        number = one + two + three + four
        transformed_nums.append(number)

    current_operands = []
    final_results = []
    for num in transformed_nums:

        if num == "+" or num == "*":
            op = num
        else:
            try:
                num = int(num)
                current_operands.append(num)
            except ValueError:
                
                if op == "+":
                    result = 0
                else:
                    result = 1

                for operand in current_operands:
                    if op == "+":
                        result += operand
                    else:
                        result *= operand

                final_results.append(result)
                current_operands = []

    # The very last entry doesn't have any spaces after it, and thus no ValueError,
    # so the calculation for those operands needs to be computed after the for loop ends.

    if op == "+":
        result = 0
    else:
        result = 1

    for operand in current_operands:
        if op == "+":
            result += operand
        else:
            result *= operand

    final_results.append(result)

    return(sum(final_results))
    


if __name__ == "__main__":
    main()