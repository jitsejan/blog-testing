import unittest
import unittest.mock as mock

try:
    from jj_classes.castle import Castle
except ModuleNotFoundError:
    import sys, os
    sys.path.insert(0, f"{os.path.dirname(os.path.abspath(__file__))}/../")
    from jj_classes.castle import Castle
from jj_classes.character import Character

class CharacterTestClass(unittest.TestCase):
    """ Defines the tests for the Character class """
    def setUp(self):
        """ Set the castle for the test cases """
        self.castle = Castle('Bowsers Castle')
        
    def test_mock_access_denied(self):
        """ Access denied for star powerup """
        mock_character = mock.Mock(powerup = 'Starman')
        self.assertFalse(self.castle.access(mock_character))
   
    def test_mock_access_granted(self):
        """ Access granted for mushroom powerup """
        mock_character = mock.Mock(powerup = 'Super Mushroom')
        self.assertTrue(self.castle.access(mock_character))
        
    def test_default_castle_boss(self):
        """ Verifty the default boss is Bowser """
        self.assertEqual(self.castle.get_boss(), "Bowser")
        
    def test_default_castle_world(self):
        """ Verify the default world is Grass Land """
        self.assertEqual(self.castle.get_world(), "Grass Land")

    # Mock a class method
    @mock.patch.object(Castle, 'get_boss')
    def test_mock_castle_boss(self, mock_get_boss):
        mock_get_boss.return_value = "Hammer Bro"
        self.assertEqual(self.castle.get_boss(), "Hammer Bro")
        self.assertEqual(self.castle.get_world(), "Grass Land")
        
    # Mock an instance
    @mock.patch(__name__+'.Castle')
    def test_mock_castle(self, MockCastle):
        instance = MockCastle
        instance.get_boss.return_value = "Toad"
        instance.get_world.return_value = "Desert Land"
        self.castle = Castle
        self.assertEqual(self.castle.get_boss(), "Toad")
        self.assertEqual(self.castle.get_world(), "Desert Land")
        
    # Mock an instance method
    def test_mock_castle_instance_method(self):
        # Boss is still Bowser
        self.assertNotEqual(self.castle.get_boss(), "Koopa Troopa")
        # Set a return_value for the get_boss method
        self.castle.get_boss = mock.Mock(return_value = "Koopa Troopa")
        # Boss is Koopa Troopa now
        self.assertEqual(self.castle.get_boss(), "Koopa Troopa")
        
    def test_castle_with_more_bosses(self):
        multi_boss_castle = mock.Mock()
        # Set a list as side_effect for the get_boss method
        multi_boss_castle.get_boss.side_effect = ["Goomba", "Boo"]
        # First value is Goomba
        self.assertEqual(multi_boss_castle.get_boss(), "Goomba")
        # Second value is Boo
        self.assertEqual(multi_boss_castle.get_boss(), "Boo")
        # Third value does not exist and raises a StopIteration
        self.assertRaises(StopIteration, multi_boss_castle.get_boss)
         
    def test_calls_to_castle(self):
        self.castle.access = mock.Mock()
        self.castle.access.return_value = "No access"
        # We should retrieve no access for everybody
        self.assertEqual(self.castle.access('Let me in'), "No access")
        self.assertEqual(self.castle.access('Let me in, please'), "No access")
        self.assertEqual(self.castle.access('Let me in, please sir!'), "No access")
        # Verify the length of the arguments list
        self.assertEqual(len(self.castle.access.call_args_list), 3)


if __name__ == '__main__':
    unittest.main()