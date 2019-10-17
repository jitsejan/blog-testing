""" jj_classes/character.py """


class Character(object):
    """ Defines the character class """

    def __init__(self, name):
        """ Initialize the class """
        self._name = name
        self._powerup = ""

    def get_powerup(self):
        """ Returns the powerup """
        return self.powerup

    @property
    def name(self):
        """ Name of the character """
        return self._name

    @property
    def powerup(self):
        """ Powerup of the character """
        return self._powerup

    @powerup.setter
    def powerup(self, powerup):
        """ Sets the powerup """
        self._powerup = powerup
