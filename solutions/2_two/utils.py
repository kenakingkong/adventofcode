is_valid_asc = lambda a, b: 0 < b - a < 4
is_valid_dsc = lambda a, b: 0 < a - b < 4

# check if all values in list match asc pattern
def is_all_valid_asc(lst):
    all([is_valid_asc(lst[i], lst[i + 1]) for i in range(0, len(lst) - 1)])


# check if all values in list match dsc pattern
def is_all_valid_dsc(lst):
    all([is_valid_dsc(lst[i], lst[i + 1]) for i in range(0, len(lst) - 1)])


# recursively check if lst matches given pattern
def check_valid(lst, func):
    if len(lst) == 1:
        return True
    if func(lst[0], lst[1]):
        return check_valid(lst[1:], func)
    return False

# return all lists with index missing
def generate_possible_lists(lst):
    results = [lst]
    length = len(lst)
    for i in range(0, length):
        results.append(lst[:i]+lst[i+1:])
    return results