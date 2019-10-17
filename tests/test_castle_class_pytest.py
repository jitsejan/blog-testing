""" tests/test_castle_class_pytest.py """
import pytest
from jj_classes.castle import Castle

class TestCastleClass:
    """ Defines the tests for the Castle class """

    def test_init_sets_name(self):
        """ Test that init sets the name """
        castle = Castle('Test name')
        assert castle.name == "Test name"

    def test_init_error_when_no_name(self):
        """ Test that init fails without the name """
        expected_error = r"__init__\(\) missing 1 required positional argument: \'name\'"
        with pytest.raises(TypeError, match=expected_error):
            castle = Castle()

    def test_has_access_true_with_super_mushroom(self, castle, character):
        """ Test that has_access returns True for Super Mushroom """
        character.powerup = 'Super Mushroom'
        assert castle.has_access(character)

    def test_has_access_false_without_super_mushroom(self, castle, character):
        """ Test that has_access returns False for other powerups """
        character.powerup = 'Not a mushroom'
        assert castle.has_access(character) is False
    
    def test_get_boss_returns_bowser(self, castle):
        """ Test that the get_boss returns Bowser """
        assert castle.get_boss() == 'Bowser'

    def test_get_world_returns_grass_land(self, castle):
        """ Test that the get_boss returns Grass Land """
        assert castle.get_world() == 'Grass Land'
