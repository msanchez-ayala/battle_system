"""
Characters
"""
import math
from dataclasses import dataclass
from enum import Enum


class DamageMultiplier(Enum):
    NOT_EFFECTIVE = 5
    NORMAL = 10
    EFFECTIVE = 20
    CRITICAL = 30


@dataclass
class Stats:
    hp: int
    attack: int
    defense: int


@dataclass
class Character:
    name: str
    stats: Stats
    lvl: int = 1
    _alive: bool = True

    def attack(self, character: 'Character') -> None:
        """
        Apply damage to opposing character.
        """
        attack = self.stats.attack  # + any buffs
        character.receive_attack(attack)

    def receive_attack(self, attack: int) -> None:
        """
        Calculate the damage to be taken from the given attack
        and subtract from hp.
        """
        damage = self._calculate_damage(attack)
        self.stats.hp -= damage
        if self.stats.hp <= 0:
            self._alive = False

    def _calculate_damage(self, attack: int) -> None:
        """
        Calculate the damage received from the given attack.
        """
        # atk=1 vs def=100 -> 1 damage
        # atk = def -> always the same amount of damage?
        # atk=100 vs def=1 -> ~99 or 100 damage
        damage = attack - self.stats.defense / attack * DamageMultiplier.NORMAL.value
        return math.ceil(damage)
