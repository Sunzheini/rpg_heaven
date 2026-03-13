"""
This is the main entry point for the game. It initializes the game options and starts the
game frontend.
"""
from core.front_end import GameFrontend
from core.options import Options


options = Options()

new_game = GameFrontend(options)
new_game.run_game()
