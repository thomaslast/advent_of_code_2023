import re
from pathlib import Path

from utils import get_input_lines

def day3_parta(file_input: Path = Path.cwd() / "input.txt") -> int:
    total = 0
    symbols = {}
    lines = get_input_lines(file_input)
    for row in range(len(lines[0]) - 1):
        for col in range(len(lines)):
            if lines[row][col] not in '0123456789.':
                symbols[(row, col)] = lines[row][col]

    for row_num, row in enumerate(lines):
        for c in re.finditer(r'\d+', row):
            possibilities = []
            for i in range(c.start() - 1, c.end() + 1):
                possibilities.append((row_num - 1, i))
                possibilities.append((row_num, i))
                possibilities.append((row_num + 1, i))
            valid = False
            for p in possibilities:
                if p in symbols:
                    valid = True
            if valid:
                total += int(c.group())
    return total

def day3_partb(file_input: Path = Path.cwd() / "input.txt") -> int:
    total = 0
    symbols = {}
    gears = {}
    lines = get_input_lines(file_input)
    for row in range(len(lines[0]) - 1):
        for col in range(len(lines)):
            if lines[row][col] not in '0123456789.':
                symbols[(row, col)] = lines[row][col]
                if lines[row][col] == '*':
                    gears[(row, col)] = []

    for row_num, row in enumerate(lines):
        for c in re.finditer(r'\d+', row):
            possibilities = []
            for i in range(c.start() - 1, c.end() + 1):
                possibilities.append((row_num - 1, i))
                possibilities.append((row_num, i))
                possibilities.append((row_num + 1, i))
            for p in possibilities:
                if p in symbols:
                    if p in gears:
                        gears[p].append(int(c.group()))

    for g in gears:
        if len(gears[g]) == 2:
            total += (gears[g][0] * gears[g][1])
    return total

if __name__ == "__main__":
    print(f"PartA: {day3_parta()}")
    print(f"PartB: {day3_partb()}")
