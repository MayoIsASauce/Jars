import pygame
pygame.init()
pygame.mixer.init()

from segments.board import create_board, draw_board, board_set, board_flag, check_win, print_board
from time import sleep


WIDTH = 6
HEIGHT = 8

window_width = 305
window_height = 408

window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Mine Sweeper")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))

# Game loop
def loop(difficulty: int):
    flag_win = False
    board = create_board(WIDTH, HEIGHT, difficulty)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    row = y // (window_height // HEIGHT)
                    col = x // (window_width // WIDTH)
                    if not board_set(board, (col, row)): running = False
                elif event.button == 3:
                    x, y = pygame.mouse.get_pos()
                    row = y // (window_height // HEIGHT)
                    col = x // (window_width // WIDTH)
                    board_flag(board, (col, row))

        window.fill((106, 91, 110))
        draw_board(window, board)
        pygame.display.flip()

        running = not (flag_win := check_win(board)) if running else False

    if flag_win:
        sound = pygame.mixer.Sound("assets/cheer.mp3")
        sound.set_volume(0.2)
        sound.play()
        sleep(3.6)
    pygame.quit()