""" jj_classes/character.py """
from typing import Optional

from pydantic import BaseModel


class Character(BaseModel):
    """Defines the character class"""

    name: str
    powerup: Optional[str]

