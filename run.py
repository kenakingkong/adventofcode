import os
import subprocess
import argparse
from nums import taken_days, num_to_words
from directory import get_dir_name


def get_args():
    parser = argparse.ArgumentParser(prog="run.py")
    parser.add_argument("-p1", "--part-one", action="store_true")
    parser.add_argument("-p2", "--part-two", action="store_true")
    parser.add_argument("day", type=int)

    args = parser.parse_args()
    day = args.day

    if day < 1 or day > 25 or day not in taken_days():
        parser.error("could not find files for day: {}".format(day))

    return args


def run_script(args):
    day = args.day
    part = "-p2" if args.part_two else "-p1"

    dir_name = get_dir_name(day)
    script_filename = os.path.join(dir_name, "script.py")
    input_filename = os.path.join(dir_name, "input.txt")

    if not os.path.exists(script_filename) or not os.path.exists(input_filename):
        print("could not find files for day: {}\n".format(day))
        os._exit(1)

    print("running: {} {}\n".format(dir_name, part))

    command = ["python3", script_filename, part, input_filename]
    result = subprocess.run(command, capture_output=True, text=True)
    answer = result.stdout.strip()
    print("Answer: {}".format(answer))


def main():
    args = get_args()
    run_script(args)


if __name__ == "__main__":
    main()
