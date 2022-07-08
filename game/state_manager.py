
from game.game_state import GameStateType
from game.states.credits_menu import CreditsMenu
from game.states.difficulty_menu import DifficultyMenu
from game.states.main_game import MainGame
from game.states.main_menu import MainMenu
from game.states.name_menu import NameMenu

class StateManager:

    def __init__(self, game):

        self.states_stack = []

        self.game = game

        self.load_states()

    def add_state(self, state):
        self.states_stack.append(state)

    def pause_state(self, state):
        for s_state in self.states_stack:
            if(type(s_state) == state):
                s_state.paused = True

    def unpause_state(self, state):
        for s_state in self.states_stack:
            if(type(s_state) == state):
                s_state.paused = False
    
    def reset_state(self, state):
        for i in range(len(self.states_stack)):
            if(type(self.states_stack[i]) == type(state)):
                self.states_stack[i] = state

    def load_states(self):

        # Window to choice player's name
        #self.add_state(NameMenu(GameStateType.SOLID, self.game))
        
        # Credits window
        self.add_state(CreditsMenu(GameStateType.SOLID, self.game, paused = True))

        # Our main menu state
        self.add_state(MainMenu(GameStateType.SOLID, self.game))

        # Chose rings window
        self.add_state(DifficultyMenu(GameStateType.SOLID, self.game))

        # Main run game state
        self.add_state(MainGame(GameStateType.SOLID, self.game))

    def update(self):
        
        for state in self.states_stack:
            if(state.paused):
                continue

            state.update()

            if(state.type == GameStateType.SOLID):
                break