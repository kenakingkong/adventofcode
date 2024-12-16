import os
import argparse
from nums import taken_days
from directory import generate_solutions_dir, get_dir_name


def get_day():
    parser = argparse.ArgumentParser(prog="generate.py")
    parser.add_argument("day", type=int, nargs=1)
    args = parser.parse_args()
    day = args.day[0]

    if day < 1 or day > 25:
        parser.error("day out of range: {}".format(day))

    if day in taken_days():
        parser.error("already created files for day: {}".format(day))

    return day


def create_and_write_files(day):
    dir_name = get_dir_name(day)
    script_filename = os.path.join(dir_name, "script.py")
    filenames = ["utils.py", "input.txt", "p1_test_input.txt", "p2_test_input.txt"]

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print("created directory: {}".format(dir_name))
    else:
        print("generate.py: error: failed to create directory: {}".format(dir_name))
        os._exit(1)

    with open(script_filename, "w") as file, open("boilerplate.py", "r") as copy_file:
        for line in copy_file:
            file.write(line)
    print("created file: {}".format(script_filename))

    for filename in filenames:
        new_filename = os.path.join(dir_name, filename)
        with open(new_filename, "w") as file:
            file.write("")
        print("created file: {}".format(new_filename))


def main():
    generate_solutions_dir()
    day = get_day()
    create_and_write_files(day)


if __name__ == "__main__":
    main()
