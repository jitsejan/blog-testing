import pytest

CASTLE_NAME = "Castle Name"
CHARACTER_NAME = "Character Name"

try:
    from jj_classes.castle import Castle
except ModuleNotFoundError:
    import sys, os

    sys.path.insert(0, f"{os.path.dirname(os.path.abspath(__file__))}/../")
    from jj_classes.castle import Castle
from jj_classes.character import Character

@pytest.fixture(scope="class")
def castle():
    return Castle(CASTLE_NAME)

@pytest.fixture(scope="class")
def character():
    return Character(CHARACTER_NAME)