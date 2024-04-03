from random import shuffle
from math import floor
import sys
import pygame

if not pygame.get_init():
    sys.stderr.write("Error, pygame not initialized before board imported!\n")
GLOBAL_FONT = pygame.font.SysFont('ComicSansMS', 25)

def get_size(board: list[list[int]]):
    return len(board[0]), len(board)

def seed_board(board: list[list[int]], dif: int):
    size = get_size(board)
    shuffle(slices := [i for i in range(len(board[0])*len(board))])
    for n in slices[:dif]:
        board[floor((n - (n % size[0])) / size[1])][n % size[0]] = 1
    return board

def create_board(width: int, height: int, dif: int):
    board = [[0 for _ in range(width)] for _ in range(height)]
    return seed_board(board, dif)

def print_board(board: list[list[int]]):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(board[r][c], end=" ")
        print()

def board_fetch(board: list[list[int]], xy: tuple[int, int]):
    return board[xy[1]][xy[0]]

def board_set(board: list[list[int]], xy: tuple[int, int]) -> bool:
    if board[xy[1]][xy[0]] == 1:
        return False
    elif board[xy[1]][xy[0]] == 0:
        board[xy[1]][xy[0]] = 2

        if bomb_check(board, xy) == 0:
            for y in range(-1, 2):
                if xy[1]+y < 0: continue
                for x in range(-1, 2):
                    if xy[0]+x < 0: continue
                    if y == 0 and x == 0: continue
                    try:
                        board_set(board, (xy[0]+x, xy[1]+y))
                    except IndexError:
                        pass

        return True
    else:
        if board[xy[1]][xy[0]] == 3:
            board[xy[1]][xy[0]] = 0
        elif board[xy[1]][xy[0]] == 4:
            board[xy[1]][xy[0]] = 1
        return True

def board_flag(board: list[list[int]], xy: tuple[int, int]):
    if board[xy[1]][xy[0]] == 0: board[xy[1]][xy[0]] = 3
    elif board[xy[1]][xy[0]] == 1: board[xy[1]][xy[0]] = 4

    elif board[xy[1]][xy[0]] == 3: board[xy[1]][xy[0]] = 0
    elif board[xy[1]][xy[0]] == 4: board[xy[1]][xy[0]] = 1

def bomb_check(board: list[list[int]], xy: tuple[int, int]):
    bombs = 0
    for y in range(-1, 2):
        if xy[1]+y < 0: continue
        for x in range(-1, 2):
            if xy[0]+x < 0: continue
            if y == 0 and x == 0: continue
            try:
                bombs += 1 if board[xy[1]+y][xy[0]+x] == 1 or board[xy[1]+y][xy[0]+x] == 4 else 0
            except IndexError:
                pass
    return bombs

def set_overlay(window: pygame.Surface, board: list[list[int]]):
    global GLOBAL_FONT
    wh = get_size(board)

    for y in range(wh[1]):
        for x in range(wh[0]):
            if board[y][x] == 2:
                if (bombs := bomb_check(board, (x,y))) > 0:
                    window.blit(GLOBAL_FONT.render(str(bombs), True, (255,255,255)), ((51*x)+15, (51*y)+10))

def draw_board(window: pygame.Surface, board: list[list[int]]):
    size = get_size(board)

    colors = {
        0: (204, 221, 183),
        1: (204, 221, 183), # <- change to: (255, 94, 91) [CHEATS]
        2: (106, 91, 110),
        3: (190, 178, 200),
        4: (190, 178, 200)
    }
    for r in range(size[1]):
        for c in range(size[0]):
            pygame.draw.rect(window, colors.get(board_fetch(board, (c, r))), [51*c, 51*r, 50, 50])
    
    set_overlay(window, board)

def check_win(board: list[list[int]]):
    win = True
    wh = get_size(board)

    for y in range(wh[1]):
        for x in range(wh[0]):
            if board[y][x] == 0 or board[y][x] == 1 or board[y][x] == 3:
                win = False
                break
        if win == False:
            break
    return win
