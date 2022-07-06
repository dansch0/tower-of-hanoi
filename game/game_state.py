
class GameStateType:
    SOLID = 1        # Will stop execute the stack     
    TRANSPARENT = 2  # The state below this type will be called

class GameState:

    def __init__(self, type, game, paused):
        self.type = type
        self.game = game
        self.paused = paused

    def update(self):
        pass