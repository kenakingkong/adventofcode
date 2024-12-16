"""
	Problem Description:
  	
    part 1:
    parse valid mul functions and run them

    part 2:


"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import parse

def parse_input_data(content):
    data = []

    for line in content:
        data.append(line)

    return data


def solve_part_one(data):
    # solve the problem with the given data
    return


def solve_part_two(data):
    # solve the problem with the given data
    return


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
