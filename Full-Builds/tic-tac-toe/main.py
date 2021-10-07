import random, time
from misc import *

while True:
    util_.clear()
    game_vars.turn = random.randint(0,1)
    while True:
        if game_methods.check_win(game_vars.players[game_vars.turn]):
            util_.clear()
            util_.printer()
            print("Player {0} wins!\n".format(game_vars.players[game_vars.turn].upper()))
            break
        if not game_vars.board.__contains__(" "):
            util_.clear()
            util_.printer()
            print("Tie!\n")
            break

        util_.clear()
        game_vars.turn = int(not bool(game_vars.turn))

        util_.printer()

        if game_vars.turn == 1:
            ai_handler.c_choose()
            continue

        move = ai_handler.get_move()

        game_methods.change_selected(game_vars.players[game_vars.turn], move)
    
    time.sleep(0.6)
    util_.restart()