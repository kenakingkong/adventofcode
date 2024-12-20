"""
	Problem Description:
  	
    part 1:
    parse valid mul functions and run them

    part 2:
    parse valid mul functions as well as do() and don't()
    only run after do() until don't()
    xxxxxdo()xxxxxxdon't()yyyyydon't()yyyydo()xxxxdo()xxxx

"""

import sys
import utils
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import parse


def parse_input_data(content):
    return "".join([line for line in content])


def solve_part_one(data):
    muls = utils.get_mul_values(data)
    return utils.mult_and_sum_nums(muls)


def solve_part_two(data):
    muls = utils.get_do_mul_values(data)
    return utils.mult_and_sum_nums(muls)


def main():
    (content, part) = parse.parse_args()

    data = parse_input_data(content)

    if part == "p1":
        answer = solve_part_one(data)
    elif part == "p2":
        answer = solve_part_two(data)

    print(answer)


if __name__ == "__main__":
    main()
