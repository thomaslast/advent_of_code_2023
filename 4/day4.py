import re
from collections import defaultdict
from pathlib import Path

from utils import get_input_lines

def day4_parta(file_input: Path = Path.cwd() / "input.txt") -> int:
    lines = get_input_lines(file_input)
    total_points = 0
    for line in lines:
        numbers, winning_numbers = line[(line.find(":")+1):].split("|")
        numbers = numbers.split()
        winning_numbers = winning_numbers.split()
        matches = 0
        for number in numbers:
            if number in winning_numbers:
                matches += 1
        if matches > 0:
            total_points += pow(2, matches-1)
    return total_points


def day4_partb(file_input: Path = Path.cwd() / "input.txt") -> int:
    lines = get_input_lines(file_input)
    cards = defaultdict(lambda: 1)
    for i, line in enumerate(lines):
        winning_numbers, numbers = line[(line.find(":")+1):].split("|")
        numbers = numbers.split()
        winning_numbers = winning_numbers.split()
        matches = 0
        for number in numbers:
            if number in winning_numbers:
                matches += 1
        for j in range(i + 1, i + 1 + matches):
            cards[j] += cards[i]
    return sum(cards.values()) + 1


if __name__ == "__main__":
    print(f"PartA: {day4_parta()}")
    print(f"PartB: {day4_partb()}")
