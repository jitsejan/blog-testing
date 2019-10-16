class Castle(object):
    def __init__(self, name):
        self.name = name
        self.boss = 'Bowser'
        self.world = 'Grass Land'

    def access(self, character):
        if character.powerup == 'Super Mushroom':
            return True
        else:
            return False
    
    def get_boss(self):
        return self.boss

    def get_world(self):
        return self.world
