# ================================================
# Project developed by Daniel Agostini Schwade
# ================================================

from game.game import Game

def main() -> None:
    
    game = Game()

    while(not game.quit_game):
        game.loop()

    game.quit()

main()
