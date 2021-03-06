""" jj_classes/castle.py """
from .character import Character
from pydantic import BaseModel


class Castle(BaseModel):
    """ Defines the Castle class """
    name: str
    boss = "Bowser"
    world = "Grass Land"

    def has_access(self, character: Character) -> bool:
        """ Check if character has access """
        return character.powerup == "Super Mushroom"
