"""
	Problem Description:
  	
    part 1:
    count how many lists have items seq asc/dec by 1-3

    part 2:
    same as part 1
    except if there is only 1 error - then add that list to the count too

"""

import sys
import utils
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import parse


def parse_input_data(content):
    data = []

    for line in content:
        data.append(list(map(int, line.split())))

    return data


def solve_part_one(data):
    count = 0
    for lst in data:
        if utils.check_valid(lst, utils.is_valid_asc):
            count += 1
        elif utils.check_valid(lst, utils.is_valid_dsc):
            count += 1
    return count


def solve_part_two(data):
    count = 0
    for lst in data:
        lsts = utils.generate_possible_lists(lst)
        for lst in lsts:
            if utils.check_valid(lst, utils.is_valid_asc):
                count += 1
                break
            elif utils.check_valid(lst, utils.is_valid_dsc):
                count += 1
                break
    return count


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
