""" tests/test_castle_class.py """
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

    # Mock a class method
    def test_mock_castle_boss(self, mocker, castle):
        """ Test that the mocked get_boss returns overwritten value """
        mock_get_boss = mocker.patch.object(Castle, "get_boss")
        mock_get_boss.return_value = "Hammer Bro"
        assert castle.get_boss(), "Hammer Bro"

    # Mock an instance
    def test_mock_castle(self, mocker):
        """ Test that the mocked instance returns overwritten values """
        instance = mocker.patch(__name__ + ".Castle")
        instance.get_boss.return_value = "Toad"
        instance.get_world.return_value = "Desert Land"
        castle = Castle
        assert castle.get_boss() == "Toad"
        assert castle.get_world() == "Desert Land"

    # Mock an instance method
    def test_mock_castle_instance_method(self, mocker, castle):
        """ Test that overwriting the instance method worked """
        # Boss is still Bowser
        assert castle.get_boss() != "Koopa Troopa"
        # Set a return_value for the get_boss method
        castle.get_boss = mocker.Mock(return_value="Koopa Troopa")
        # Boss is Koopa Troopa now
        assert castle.get_boss() == "Koopa Troopa"

    def test_castle_with_more_bosses(self, mocker):
        """ Test that get_boss gets overwritten several times """
        multi_boss_castle = mocker.Mock()
        # Set a list as side_effect for the get_boss method
        multi_boss_castle.get_boss.side_effect = ["Goomba", "Boo"]
        # First value is Goomba
        assert multi_boss_castle.get_boss() == "Goomba"
        # Second value is Boo
        assert multi_boss_castle.get_boss() == "Boo"
        # Third value does not exist and raises a StopIteration
        with pytest.raises(StopIteration):
            multi_boss_castle.get_boss()

    def test_calls_to_castle(self, mocker, castle):
        """ Test that has_access gets called 3 times """
        castle.has_access = mocker.Mock()
        castle.has_access.return_value = "No access"
        # We should retrieve no access for everybody
        assert castle.has_access("Let me in") == "No access"
        assert castle.has_access("Let me in, please") == "No access"
        assert castle.has_access("Let me in, please sir!") == "No access"
        # Verify the length of the arguments list
        assert len(castle.has_access.call_args_list) == 3
