"""
Characters
"""
import math
from dataclasses import dataclass
from enum import Enum

MAX_STATS_VAL = 100


class DamageMultiplier(Enum):
    NOT_EFFECTIVE = 5
    NORMAL = 0.5
    EFFECTIVE = 20
    CRITICAL = 30


@dataclass
class Stats:
    hp: int
    attack: int
    defense: int
    speed: int


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
            self.stats.hp = 0

    def _calculate_damage(self, attack: int) -> int:
        """
        Calculate the damage received from the given attack.
        """
        adjusted_def = MAX_STATS_VAL - self.stats.defense
        def_buff = (attack - adjusted_def * attack / MAX_STATS_VAL)
        damage = attack - DamageMultiplier.NORMAL.value * def_buff
        return math.floor(damage)
