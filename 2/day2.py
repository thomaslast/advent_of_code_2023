from pathlib import Path
import regex as re
from utils import get_input_lines, max_numbers

results = {}


def day2_parta(file_input: Path = Path.cwd() / "input.txt") -> int:
    input_lines = get_input_lines(file_input)

    for line in input_lines:
        game_id = int(re.findall(f"Game ([0-9]+)", line)[0])
        results[game_id] = {}
        results[game_id]["red"] = max_numbers(line, "red")
        results[game_id]["green"] = max_numbers(line, "green")
        results[game_id]["blue"] = max_numbers(line, "blue")
    game_id_total = 0
    for game_id, colours in results.items():
        if colours["red"] <= 12 and colours["green"] <= 13 and colours["blue"] <= 14:
            game_id_total += game_id

    return game_id_total


def day2_partb(file_input: Path = Path.cwd() / "input.txt") -> int:
    input_lines = get_input_lines(file_input)

    for line in input_lines:
        game_id = int(re.findall(f"Game ([0-9]+)", line)[0])
        results[game_id] = {}
        results[game_id]["red"] = max_numbers(line, "red")
        results[game_id]["green"] = max_numbers(line, "green")
        results[game_id]["blue"] = max_numbers(line, "blue")
    total_powers = 0
    for _, colours in results.items():
        total_powers += colours["red"] * colours["blue"] * colours["green"]

    return total_powers



if __name__ == "__main__":
    print(f"PartA: {day2_parta()}")
    print(f"PartB: {day2_partb()}")
