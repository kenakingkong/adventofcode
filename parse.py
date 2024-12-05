import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p1", "--part-one", action='store_true')
    parser.add_argument("-p2", "--part-two", action='store_true')
    parser.add_argument("input_file", type=argparse.FileType("r"))

    args = parser.parse_args()
    input_file = args.input_file
    part = "p2" if args.part_two else "p1"
    return (input_file, part)
