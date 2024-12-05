import os
import subprocess
import argparse
from utils import taken_days, num_to_words


def get_day():
    parser = argparse.ArgumentParser(prog="generate.py")
    parser.add_argument("day", type=int)
    args = parser.parse_args()
    day = args.day

    if day < 1 or day > 25 or day not in taken_days():
        parser.error("could not find files for day: {}".format(day))

    return day


def run_test(script_filename, test_filename, temp_filename):
    with open(test_filename, "r") as fin:
        data = fin.read().splitlines(True)

    with open(temp_filename, "w") as fout:
        fout.writelines(data[1:])

    command = ["python3", script_filename, temp_filename]
    result = subprocess.run(command, capture_output=True, text=True)
    answer = result.stdout.strip()
    
    os.remove(temp_filename)

    if int(answer) == int(data[0]):
        print("{}: Success".format(test_filename))
    else:
        print("{}: Failed ({} != {})".format(test_filename, int(answer), int(data[0])))


def run_script(day):
    dir_name = "day/{}".format(num_to_words[day])
    script_filename = os.path.join(dir_name, "script.py")

    files = os.listdir(dir_name)
    test_files = list(filter(lambda f: f.startswith("test_"), files))

    if not os.path.exists(script_filename) or not test_files:
        print("could not find files for day: {}\n".format(day))
        os._exit(1)

    print("running tests: {}\n".format(dir_name))

    for file in test_files:
        test_filename = os.path.join(dir_name, file)
        temp_filename = os.path.join(dir_name, "temp_{}".format(file))
        run_test(script_filename, test_filename, temp_filename)


def main():
    day = get_day()
    run_script(day)


if __name__ == "__main__":
    main()
