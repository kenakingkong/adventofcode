import os

word_to_nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "twenty_one": 21,
    "twenty_two": 22,
    "twenty_three": 23,
    "twenty_four": 24,
    "twenty_five": 25,
}

num_to_words = {v: k for k, v in word_to_nums.items()}


def taken_days():
    days = []
    for filename in os.scandir("day"):
        days.append(word_to_nums[filename.path.split("/")[1]])
    return days
