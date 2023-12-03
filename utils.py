import regex as re


def get_input_lines(file):
    with open(file) as f:
        return f.readlines()


def get_input_lines_as_lists(file):
    with open(file) as f:
        return [x.split() for x in f.readlines()]


def total_numbers(line, colour):
    matches = re.findall(f"([0-9]+) {colour}", line)
    return sum([int(x) for x in matches])


def max_numbers(line, colour):
    matches = re.findall(f"([0-9]+) {colour}", line)
    return max([int(x) for x in matches])


def min_numbers(line, colour):
    matches = re.findall(f"([0-9]+) {colour}", line)
    return min([int(x) for x in matches])
