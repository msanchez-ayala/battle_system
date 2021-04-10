import pytest

from battle_system import character


class TestCharacter:

    def setup(self):
        pogue_stats = character.Stats(50, 40, 20)
        sivan_stats = character.Stats(50, 30, 30)
        self.pogue = character.Character('Pogue', pogue_stats)
        self.sivan = character.Character('Steve', sivan_stats)

    def test_can_init(self):
        assert True

    def test_receive_attack(self):
        self.pogue.attack(self.sivan)
        assert self.sivan.stats.hp < 50
        assert self.sivan._alive is True

        self.pogue.attack(self.sivan)
        assert self.sivan.stats.hp == 0
        assert self.sivan._alive is False

    @pytest.mark.skip
    def test__calculate_damage(self):
        # assert self.pogue._calculate_damage(30) == 24
        # FIXME this fails
        # assert self.pogue._calculate_damage(10) ==
        for attack in range(1,11):
            for defense in range(1,11):
                stats_1 = character.Stats(100, attack*10, 0)
                stats_2 = character.Stats(100, 0, defense*10)
                char_1 = character.Character('Pogue', stats_1)
                char_2 = character.Character('Sivan', stats_2)

                print(f' Attack: {char_1.stats.attack} Defense: {char_2.stats.defense} Damage: {char_2._calculate_damage(char_1.stats.attack)}')