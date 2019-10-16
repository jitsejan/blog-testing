import unittest
import unittest.mock as mock

try:
    from jj_classes.castle import Castle
except ModuleNotFoundError:
    import sys, os

    sys.path.insert(0, f"{os.path.dirname(os.path.abspath(__file__))}/../")
    from jj_classes.castle import Castle
from jj_classes.character import Character


class CharacterCastleTestClass(unittest.TestCase):
    """ Defines the tests for the Character and Castle class together """

    @mock.patch(__name__ + ".Castle")
    @mock.patch(__name__ + ".Character")
    def test_mock_castle_and_character(self, MockCharacter, MockCastle):
        # Note the order of the arguments of this test
        MockCastle.name = "Mocked Castle"
        MockCharacter.name = "Mocked Character"
        self.assertEqual(Castle.name, "Mocked Castle")
        self.assertEqual(Character.name, "Mocked Character")

    def test_fake_powerup(self):
        character = Character("Sentinel Character")
        character.powerup = mock.Mock()
        character.powerup.return_value = mock.sentinel.fake_superpower
        self.assertEqual(character.powerup(), mock.sentinel.fake_superpower)

    def test_castle_with_more_powerups(self):
        self.castle = Castle("Beautiful Castle")
        multi_characters = mock.Mock()
        # Set a list as side_effect for the get_boss method
        multi_characters.get_powerup.side_effect = ["mushroom", "star"]
        # First value is mushroom
        self.assertEqual(multi_characters.get_powerup(), "mushroom")
        # Second value is star
        self.assertEqual(multi_characters.get_powerup(), "star")
        # Third value does not exist and raises a StopIteration
        self.assertRaises(StopIteration, multi_characters.get_powerup)


if __name__ == "__main__":
    unittest.main()
