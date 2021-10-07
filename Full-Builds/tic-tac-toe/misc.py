import os, random
class game_vars():
    turn = 0
    players = ["x","o"]
    board = [" "," "," ",
             " "," "," ",
             " "," "," "]
    open_moves = [0,1,2,
                3,4,5,
                6,7,8]
    winning_moves_x = [[0,1,2],[3,4,5],[6,7,8], # left-right
                    [0,3,6],[1,4,7],[2,5,8], # up-down
                    [0,4,8],[2,4,6]]         # Diag
    winning_moves_y = [[0,1,2],[3,4,5],[6,7,8], # left-right
                    [0,3,6],[1,4,7],[2,5,8], # up-down
                    [0,4,8],[2,4,6]]         # Diag

class ai_handler():
    @staticmethod
    def ai_challenge() -> int:
        for i in range(len(game_vars.winning_moves_y)):
            if len(game_vars.winning_moves_y[i]) == 1:
                return game_vars.winning_moves_y[i][0]
        for i in range(len(game_vars.winning_moves_x)):
            if len(game_vars.winning_moves_x[i]) == 1:
                to_return:int = game_vars.winning_moves_x[i][0]
                game_vars.winning_moves_x.remove(game_vars.winning_moves_x[i])
                return to_return
        return game_vars.open_moves[random.randint(0,len(game_vars.open_moves)-1)]
    @staticmethod
    def c_choose()->None:
        comp_chose:int = ai_handler.ai_challenge()
        err_count:int = 0
        while not game_methods.check_move(comp_chose):
            game_methods.remove_open(comp_chose, game_vars.players[1])
            if err_count < 3: print("stuck")
            comp_chose = ai_handler.ai_challenge()
            err_count += 1
        game_methods.change_selected(game_vars.players[1], comp_chose)
    @staticmethod
    def get_move()->int:
        for i in range(len(game_vars.winning_moves_x)):
            if len(game_vars.winning_moves_x[i]) == 1:
                return game_vars.winning_moves_x[i][0]
        for i in range(len(game_vars.winning_moves_y)):
            if len(game_vars.winning_moves_y[i]) == 1:
                to_return:int = game_vars.winning_moves_y[i][0]
                game_vars.winning_moves_y.remove(game_vars.winning_moves_y[i])
                return to_return
        move_buffer = game_vars.open_moves[random.randint(0,len(game_vars.open_moves)-1)]
        while not game_methods.check_move(move_buffer):
            move_buffer = game_vars.open_moves[random.randint(0,len(game_vars.open_moves)-1)]
        return move_buffer

class game_methods():
    @staticmethod
    def check_win(player):
        for i in range(9):
            if i == 0 or i % 3 == 0:
                if game_vars.board[i] == player and game_vars.board[i+1] == player and game_vars.board[i+2] == player:
                    return True
        if (game_vars.board[4] == player):
            if (game_vars.board[0] == player and game_vars.board[8] == player) or (game_vars.board[2] == player and game_vars.board[6] == player):
                return True
        for i in range(3):
            if game_vars.board[i] == player and game_vars.board[i+3] == player and game_vars.board[i+6] == player:
                return True
        return False
    @staticmethod
    def remove_open(index:int, player:str):
        try: game_vars.open_moves.remove(index)
        except ValueError: 
            if not game_vars.open_moves.__contains__(index): pass
            print("Cannot remove: {0} from {1}".format(index, str(game_vars.open_moves)))
        if player == game_vars.players[0]:
            for i in range(len(game_vars.winning_moves_x)):
                for j in game_vars.winning_moves_x[i]:
                    if index == j: game_vars.winning_moves_x[i].remove(index)
        elif player == game_vars.players[1]:
            for i in range(len(game_vars.winning_moves_y)):
                for j in game_vars.winning_moves_y[i]:
                    if index == j: game_vars.winning_moves_y[i].remove(index)
    @staticmethod
    def check_move(position):
        return False if game_methods.get_selected(position) != " " else True
    @staticmethod
    def change_selected(player, index):
        switcher = {0:6, 1:7, 2:8, 3:3, 4:4, 5:5, 6:0, 7:1, 8:2}
        game_vars.board[switcher.get(index)] = player
        game_methods.remove_open(index, player)
    @staticmethod
    def get_selected(index):
        if index < 0 or index > 8: return "ERR"
        switcher = {0:6, 1:7, 2:8, 3:3, 4:4, 5:5, 6:0, 7:1, 8:2}
        return game_vars.board[switcher.get(index)]

class util_():
    @staticmethod
    def clear():
        if os.name == 'nt': os.system("cls")
        else: os.system('clear')
    @staticmethod
    def printer():
        print("Player {0}\'s turn!".format(game_vars.players[game_vars.turn].upper()))
        for i in range(9):
            print(game_vars.board[i], end="", flush=True)
            bug_fix = i+1
            if bug_fix%3 == 0:
                print("")
                continue
            print(" | ", end="", flush=True)
    @staticmethod
    def restart():
        game_vars.board = [" "," "," ",
                           " "," "," ",
                           " "," "," "]
        game_vars.open_moves = [0,1,2,3,4,5,6,7,8]

        game_vars.turn = 0
