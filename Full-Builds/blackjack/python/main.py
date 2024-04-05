import pygame, sys, json

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blackjack")

def read_pipe() -> str:
    returnable = ""
    while True:
        c = sys.stdin.read(1)
        if str(c) == "\n": break
        else:
            returnable += c
        sys.stdin.flush
    return returnable

data = read_pipe()
object_ = json.loads(data)

background = tuple(map(int, object_['background'].split(", ")))
player = object_['player']

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)

    data = read_pipe()
    if str(data) == "-1!":
        running = False
    else:
        object_ = json.loads(data)
        player = object_['player']

    pygame.draw.rect(screen, tuple(player['color']),    
                     pygame.Rect(player['x'], player['y'], player['w'], player['h'])
    )

    pygame.display.flip()

# Quit Pygame
pygame.quit()