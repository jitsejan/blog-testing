import pytest

try:
    from jj_classes.castle import Castle
except ModuleNotFoundError:
    import sys, os

    sys.path.insert(0, f"{os.path.dirname(os.path.abspath(__file__))}/../")
    from jj_classes.castle import Castle
from jj_classes.character import Character


class TestCharacterClass:
    """ Defines the tests for the Character class """

    def setup_class(self):
        """ Set the castle for the test cases """
        self.castle = Castle("Bowsers Castle")

    def test_mock_access_denied(self, mocker):
        """ Access denied for star powerup """
        mock_character = mocker.Mock(powerup="Starman")
        assert self.castle.has_access(mock_character) is False

    def test_mock_access_granted(self, mocker):
        """ Access granted for mushroom powerup """
        mock_character = mocker.Mock(powerup="Super Mushroom")
        assert self.castle.has_access(mock_character)

    def test_default_castle_boss(self):
        """ Verifty the default boss is Bowser """
        assert self.castle.get_boss() == "Bowser"

    def test_default_castle_world(self):
        """ Verify the default world is Grass Land """
        assert self.castle.get_world(), "Grass Land"

    # Mock a class method
    def test_mock_castle_boss(self, mocker):
        mock_get_boss = mocker.patch.object(Castle, "get_boss")
        mock_get_boss.return_value = "Hammer Bro"
        assert self.castle.get_boss(), "Hammer Bro"
        assert self.castle.get_world(), "Grass Land"

    # Mock an instance
    def test_mock_castle(self, mocker):
        instance = mocker.patch(__name__ + ".Castle")
        instance.get_boss.return_value = "Toad"
        instance.get_world.return_value = "Desert Land"
        self.castle = Castle
        assert self.castle.get_boss() == "Toad"
        assert self.castle.get_world() == "Desert Land"

    # Mock an instance method
    def test_mock_castle_instance_method(self, mocker):
        # Boss is still Bowser
        assert self.castle.get_boss() != "Koopa Troopa"
        # Set a return_value for the get_boss method
        self.castle.get_boss = mocker.Mock(return_value="Koopa Troopa")
        # Boss is Koopa Troopa now
        assert self.castle.get_boss() == "Koopa Troopa"

    def test_castle_with_more_bosses(self, mocker):
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

    def test_calls_to_castle(self, mocker):
        self.castle.has_access = mocker.Mock()
        self.castle.has_access.return_value = "No access"
        # We should retrieve no access for everybody
        assert self.castle.has_access("Let me in") == "No access"
        assert self.castle.has_access("Let me in, please") == "No access"
        assert self.castle.has_access("Let me in, please sir!") == "No access"
        # Verify the length of the arguments list
        assert len(self.castle.has_access.call_args_list) == 3
