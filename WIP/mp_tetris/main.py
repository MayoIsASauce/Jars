import pygame
from time import time
from classes.Pieces import p_Long, p_Square, Piece, Square
from classes.GridManager import GridManager, GridPiece

pygame.init()

# Set up the drawing window
d_info = pygame.display.Info()
screen = pygame.display.set_mode([d_info.current_w-300, d_info.current_h-300])

pygame.display.set_caption('SUPER COOL TETRIX')

# Run until the user asks to quit
running = True

p_dict: dict[Piece] = {
    0: p_Square(7, 76.0),
    1: p_Long(101.0, 76.0)
}

grid_man = GridManager()
grid_man.spawnObject(GridPiece.tPiece, (1,0))

print(grid_man.__str__())
quit()

grid = []
for y in range(10):
    for x in range(24):
        if x == 11 or x == 12:
            grid.append(Square((104, 97, 133), 7+(x*47.0), 125+(y*47.0)))
        else:
            grid.append(Square((88, 82, 110), 7+(x*47.0), 125+(y*47.0)))

speed = 1
move_lock = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((75, 70, 94))

    for g in grid:
        pygame.draw.rect(screen, g.color, g.getRect(), border_radius=2)

    for p in list(p_dict.values()):
        for s in p.squares:
            pygame.draw.rect(screen, s.color, s.getRect(), border_radius=2)

    pygame.display.flip()

    if time() > move_lock:
        for p in list(p_dict.values()):
            p.moveAllY(47.0)
        move_lock = time()+(1/speed)

pygame.quit()