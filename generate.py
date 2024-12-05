import os
import argparse
from utils import num_to_words, taken_days


def generate_day_directory():
    if not os.path.exists("day"):
        os.mkdir("day")


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
    dir_name = "day/{}".format(num_to_words[day])
    script_filename = os.path.join(dir_name, "script.py")
    input_filename = os.path.join(dir_name, "input.txt")
    test_input_filename = os.path.join(dir_name, "test_input.txt")

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

    with open(input_filename, "w") as file:
        file.write("")

    print("created file: {}".format(input_filename))

    with open(test_input_filename, "w") as file:
        file.write("")

    print("created file: {}".format(test_input_filename))



def main():
    generate_day_directory()
    day = get_day()
    create_and_write_files(day)


if __name__ == "__main__":
    main()
