import os
import argparse
from utils import taken_days, num_to_words

def get_day():
    parser = argparse.ArgumentParser(prog="generate.py")
    parser.add_argument("day", type=int, nargs=1)
    args = parser.parse_args()
    day = args.day[0]

    if day < 1 or day > 25 or day not in taken_days():
        parser.error("could not find files for day: {}".format(day))

    return day


def run_script(day):
    dir_name = "day/{}".format(num_to_words[day])
    script_filename = os.path.join(dir_name, "script.py")
    input_filename = os.path.join(dir_name, "input.txt")

    if not os.path.exists(script_filename) or not os.path.exists(input_filename):
        print("could not find files for day: {}\n".format(day))
        os._exit(1)
    else:
        print("running: {}\n".format(dir_name))
        os.system("python3 {} {}".format(script_filename, input_filename))


def main():
    day = get_day()
    run_script(day)


if __name__ == "__main__":
    main()
