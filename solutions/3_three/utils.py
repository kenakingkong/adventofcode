import re

"""
parsing
"""

# return list from matrix
flatten_list = lambda lst: [item for sublist in lst for item in sublist]

# return list of matches for "mul(d,d)" in the given string
find_muls = lambda txt: re.findall(r"mul\(\d{1,3},\d{1,3}\)", txt)

# return 3 digit numbers in mul
grab_mul_values = lambda txt: re.findall(r"\d{1,3}", txt)

# return [d,d] integers from [d,d] strings
grab_int_values = lambda vals: list(map(int, vals))

# return [d,d] integers from 3 digit numbers in mul
grab_int_mul_values = lambda txt: grab_int_values(re.findall(r"\d{1,3}", txt))


# return list of lists of mul numbers from string
def get_mul_values(str):
    return list(map(grab_int_mul_values, find_muls(str)))


# return list of lists of mul numbers between dos/donts
def get_do_mul_values(str):
    muls = []

    # split at do()
    broken_at_do = str.split("do()")

    for maybe_dos in broken_at_do:
        # remove everything following don't()
        bad_muls = re.sub(r"don't\(\)[\s\S]+", "", maybe_dos)
        muls.append(get_mul_values(bad_muls))

    return flatten_list(muls)


"""
arithmetics
"""

mult_nums = lambda vals: vals[0] * vals[1]
mult_and_sum_nums = lambda lst: sum(list(map(mult_nums, lst)))
