import os
from nums import num_to_words


def get_dir_name(day):
    return "solutions/{}_{}".format(day, num_to_words[day])


def generate_solutions_dir():
    if not os.path.exists("solutions"):
        os.mkdir("solutions")
