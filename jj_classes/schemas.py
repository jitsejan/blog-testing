from pydantic import BaseModel
from typing import List, Optional


class Character(BaseModel):
    """Defines the Character class"""

    name: str


class CharacterInGame(Character):
    """Defines the Character in Game class"""
    lives: int
    powerups: Optional[List[str]] = []


class Enemy(BaseModel):
    """Defines the Enemy class"""

    name: str


class Item(BaseModel):
    """Defines the Item class"""
    name: str


class World(BaseModel):
    """Defines the World class"""
    name: str
