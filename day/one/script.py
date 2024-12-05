"""
	Problem Description:
  	get sum of distances across the pair of lists row by row - ordered ascending
    ex) abs(l1[0]-l2[0]) + abs(l1[1]-l2[1]) + ...
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import utils


def parse_input_file():
    content = utils.open_input_file()

    data = [[], []]

    for line in content:
        [x, y] = line.split()
        data[0].append(int(x))
        data[1].append(int(y))

    return data


def solve_problem(data):
    sum = 0

    [lst_x, lst_y] = data
    lst_x.sort()
    lst_y.sort()

    for i in range(0, len(lst_x)):
        sum += abs(lst_x[i] - lst_y[i])

    return sum


def main():
    data = parse_input_file()
    answer = solve_problem(data)
    print(answer)
    return answer


if __name__ == "__main__":
    main()
