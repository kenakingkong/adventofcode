"""
	Problem Description:
  	---
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import utils


def parse_input_file():
    content = utils.open_input_file()

    # create data structure
    # fit content into data structure

    data = None
    return data


def solve_problem(data):
    # solve the problem with the given data
    return


def main():
    data = parse_input_file()
    answer = solve_problem(data)
    print("Answer: {}".format(answer))


if __name__ == "__main__":
    main()
