import sys
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

def init_window(pygame, size: tuple[int, ...]):
    pygame.init()

    screen = pygame.display.set_mode(size=(size[0], size[1])) # pylance aneurism
    pygame.display.set_caption("Blackjack")

    return screen
