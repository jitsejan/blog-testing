from .schemas import Character, Enemy, Item
from yaml import safe_load, YAMLError
from typing import Dict, List


class Game:
    """Defines the Game class"""
    def __init__(self, yaml_file: str):
        data = self._load_yaml(filename=yaml_file)
        self._name = data['name']
        self._characters = [self.get_character(c) for c in data['characters']]
        self._enemies = [self.get_enemy(e) for e in data['enemies']]
        self._items = [self.get_item(i) for i in data['items']]

    @staticmethod
    def _load_yaml(filename: str) -> Dict:
        with open(filename, "r") as stream:
            try:
                return safe_load(stream)
            except YAMLError as exc:
                raise (exc)
    
    @staticmethod
    def get_character(name: str) -> Character:
        return Character(
            name=name
        )

    @staticmethod
    def get_enemy(name: str) -> Enemy:
        return Enemy(
            name=name
        )

    @staticmethod
    def get_item(name: str) -> Item:
        return Item(
            name=name
        )

    @property
    def characters(self) -> List[Character]:
        return self._characters

    @property
    def enemies(self) -> List[Enemy]:
        return self._enemies
    
    @property
    def items(self) -> List[Item]:
        return self._items

    @property
    def name(self):
        return self._name
