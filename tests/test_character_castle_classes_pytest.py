import pytest

try:
    from jj_classes.castle import Castle
except ModuleNotFoundError:
    import sys, os

    sys.path.insert(0, f"{os.path.dirname(os.path.abspath(__file__))}/../")
    from jj_classes.castle import Castle
from jj_classes.character import Character


class TestCharacterCastle:
    """ Defines the tests for the Character and Castle class together """

    def test_mock_castle_and_character(self, mocker):
        # Note the order of the arguments of this test
        mock_character = mocker.patch(__name__ + ".Character")
        mock_castle = mocker.patch(__name__ + ".Castle")
        mock_castle.name = "Mocked Castle"
        mock_character.name = "Mocked Character"
        assert Castle.name == "Mocked Castle"
        assert Character.name == "Mocked Character"

    def test_fake_powerup(self, mocker):
        character = Character("Sentinel Character")
        character.powerup = mocker.Mock()
        character.powerup.return_value = mocker.sentinel.fake_superpower
        assert character.powerup() == mocker.sentinel.fake_superpower

    def test_castle_with_more_powerups(self, mocker):
        self.castle = Castle("Beautiful Castle")
        multi_characters = mocker.Mock()
        # Set a list as side_effect for the get_boss method
        multi_characters.get_powerup.side_effect = ["mushroom", "star"]
        # First value is mushroom
        assert multi_characters.get_powerup() == "mushroom"
        # Second value is star
        assert multi_characters.get_powerup() == "star"
        # Third value does not exist and raises a StopIteration
        with pytest.raises(StopIteration):
            multi_characters.get_powerup()
