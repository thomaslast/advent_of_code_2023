from pathlib import Path
from day2 import day2


def test_examples_1():
    assert day2(Path.cwd() / "test_input.txt") == 9
