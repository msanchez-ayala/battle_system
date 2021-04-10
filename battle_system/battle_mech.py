from typing import List

from character import Character


class Turn:
    """
    1 character performing actions in a single turn of battle.

    TODO: Do we allow character to move multiple times?
    TODO: How many actions are allowed?
            Does this include all actions or just non-move actions?
    """
    turn_idx: int
    character: Character
    num_moves: int
    _num_actions: int = 1


class Round:
    """
    A single round of turns
    """
    characters: List[Character]
    pass


class Battle:
    """
    Controls all turns and information of a single battle.
    """
    pass