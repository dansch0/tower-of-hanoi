
from game.game_state import GameState

import pygame
from game.constants import *
from game.game_state import *
from game.gui.button import Button


class DifficultyMenu(GameState):
    def __init__(self, type, game, paused = False):
        super().__init__(type, game, paused)

    def update(self):
        pass