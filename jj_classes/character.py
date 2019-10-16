class Character(object):
    def __init__(self, name):
        self.name = name
        self.powerup = ''

    def powerup(self, powerup):
        self.powerup = powerup

    def get_powerup(self):
        return self.powerup