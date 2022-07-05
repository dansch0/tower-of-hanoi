
class GameStateType:
    SOLID = 1       # Will stop execute the stack     
    TRANSPARENT = 2 # The state below this type will be called

class GameState:

    paused = False

    def __init__(self, type, game):
        self.type = type
        self.game = game

    def update():
        pass