""" tests/test_character_class.py """
import pytest
from jj_classes.character import Character

class TestCharacterClass:
    """ Defines the tests for the Character class """

    def test_init_sets_name(self):
        """ Test that init sets the name """
        character = Character('Test name')
        assert character.name == "Test name"

    def test_init_error_when_no_name(self):
        """ Test that init fails without the name """
        expected_error = r"__init__\(\) missing 1 required positional argument: \'name\'"
        with pytest.raises(TypeError, match=expected_error):
            character = Character()

    def test_get_powerup_returns_correct_value_when_not_set(self, character):
        """ Test that the get_powerup returns the right value when not set """
        assert character.get_powerup() == ""

    def test_get_powerup_returns_correct_value_when_set(self, character):
        """ Test that the get_powerup returns the right value when set """
        character.powerup = "Fire Flower"
        assert character.get_powerup() == "Fire Flower"

    def test_fake_powerup(self, mocker, character):
        """ Test that the powerup can be mocked """
        character.powerup = mocker.Mock()
        character.powerup.return_value = mocker.sentinel.fake_superpower
        assert character.powerup() == mocker.sentinel.fake_superpower

    def test_characters_with_more_powerups(self, mocker, castle):
        """ Test that get_powerup gets overwritten several times """
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
