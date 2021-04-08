import pytest

from battle_system import character


class TestCharacter:

    def setup(self):
        pogue_stats = character.Stats(100, 40, 20)
        sivan_stats = character.Stats(100, 30, 30)
        self.pogue = character.Character('Pogue', pogue_stats)
        self.sivan = character.Character('Steve', sivan_stats)

    def test_can_init(self):
        assert True

    def test__calculate_damage(self):
        assert self.pogue._calculate_damage(30) == 24
        # FIXME this fails
        # assert self.pogue._calculate_damage(10) == 5



