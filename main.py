from core.front_end import GameFrontend
from core.options import Options


options = Options()

new_game = GameFrontend(options)
new_game.run_game()
