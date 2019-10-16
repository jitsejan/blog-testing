""" jj_classes/castle.py """


class Castle(object):
    """ Defines the Castle class """

    def __init__(self, name):
        """ Initialize the class """
        self._name = name
        self._boss = "Bowser"
        self._world = "Grass Land"

    def has_access(self, character):
        """ Check if character has access """
        return character.powerup == "Super Mushroom"

    def get_boss(self):
        """ Returns the boss """
        return self.boss

    def get_world(self):
        """ Returns the world """
        return self.world

    @property
    def name(self):
        """ Name of the castle """
        return self._name

    @property
    def boss(self):
        """ Boss of the castle """
        return self._boss

    @property
    def world(self):
        """ World of the castle """
        return self._world
