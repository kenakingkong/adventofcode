import os
import subprocess
import argparse
from nums import taken_days
from directory import get_dir_name


def get_args():
    parser = argparse.ArgumentParser(prog="generate.py")
    parser.add_argument("-p1", "--part-one", action="store_true")
    parser.add_argument("-p2", "--part-two", action="store_true")
    parser.add_argument("day", type=int)

    args = parser.parse_args()
    day = args.day

    if day < 1 or day > 25 or day not in taken_days():
        parser.error("could not find files for day: {}".format(day))

    return args


def run_test(script_filename, flag, test_filename, temp_filename):
    with open(test_filename, "r") as fin:
        data = fin.read().splitlines(True)

    with open(temp_filename, "w") as fout:
        fout.writelines(data[1:])

    command = ["python3", script_filename, flag, temp_filename]
    result = subprocess.run(command, capture_output=True, text=True)
    answer = result.stdout.strip()

    os.remove(temp_filename)

    if int(answer) == int(data[0]):
        print("{}: Success".format(test_filename))
    else:
        print("{}: Failed ({} != {})".format(test_filename, int(answer), int(data[0])))


def run_script(args):
    day = args.day
    prefix = "p2_test_" if args.part_two else "p1_test_"
    flag = "-p2" if args.part_two else "-p1"
    dir_name = get_dir_name(day)
    script_filename = os.path.join(dir_name, "script.py")

    files = os.listdir(dir_name)
    test_files = list(filter(lambda f: f.startswith(prefix), files))

    if not os.path.exists(script_filename) or not test_files:
        print("could not find files for day: {}\n".format(day))
        os._exit(1)

    print("running tests: {} {}\n".format(dir_name, flag))

    for file in test_files:
        test_filename = os.path.join(dir_name, file)
        temp_filename = os.path.join(dir_name, "temp_{}".format(file))
        run_test(script_filename, flag, test_filename, temp_filename)


def main():
    args = get_args()
    run_script(args)


if __name__ == "__main__":
    main()
