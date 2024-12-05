"""
	Problem Description:

    part 1:
  	get sum of distances across the pair of lists row by row - ordered ascending
    ex) abs(l1[0]-l2[0]) + abs(l1[1]-l2[1]) + ...

    part 2:
    sum the similarity scores of the items in the left list
    mult each item in the left list by how many time it occurs in the right list
    ex) l1[0] * x + ....
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import parse


def parse_input_data(content):
    data = [[], []]

    for line in content:
        [x, y] = line.split()
        data[0].append(int(x))
        data[1].append(int(y))

    return data


def solve_part_one(data):
    sum = 0

    [lst_x, lst_y] = data
    lst_x.sort()
    lst_y.sort()

    for i in range(0, len(lst_x)):
        sum += abs(lst_x[i] - lst_y[i])

    return sum


def solve_part_two(data):
    sum = 0
    score_dict = {}

    [lst_x, lst_y] = data
    for num in lst_x:
        if num in score_dict:
            sum += score_dict[num]
            continue

        count = len(list(filter(lambda n: n == num, lst_y)))
        score_dict[num] = num * count
        sum += num * count

    return sum


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
