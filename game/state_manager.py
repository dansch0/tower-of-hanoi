
from game.game_state import GameStateType
from game.states.main_game import MainGame
from game.states.main_menu import MainMenu

class StateManager:

    states_stack = []

    def __init__(self, game):
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
        for s_state in self.states_stack:
            if(type(s_state) == state):
                s_state = state(s_state.type)

    def load_states(self):
        
        # Our main menu state
        self.add_state(MainMenu(GameStateType.SOLID, self.game))

        # Main run game state
        self.add_state(MainGame(GameStateType.SOLID, self.game))

    def update(self):
        
        for state in self.states_stack:
            if(state.paused):
                continue

            state.update()

            if(state.type == GameStateType.SOLID):
                break