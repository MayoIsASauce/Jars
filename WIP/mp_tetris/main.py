import pygame

from time import time
from random import randint

from classes.GridManager import GridManager, GridPiece, color_dict, lowest_square, right_square, left_square

pygame.init()

# Set up the drawing window
d_info = pygame.display.Info()
screen = pygame.display.set_mode([d_info.current_w-300, d_info.current_h-300])

pygame.display.set_caption('SUPER COOL TETRIX')

# Run until the user asks to quit
running = True

p_sequential = 0
p_dict: dict[int, tuple[GridPiece, tuple[int,int], int]] = {}

columns = {}
rows = {}

for i in range(24):
    columns[i] = 8.0 + (47*i)
for i in range(10):
    rows[i] = 123 + (47*i)

grid_man = GridManager()

def create_object(gridPiece:GridPiece, xy:tuple[int,int]):
    global p_sequential
    x, y = xy

    p_dict[p_sequential] = (gridPiece, (x,y), 0)
    grid_man.editObject(gridPiece, (x,y), 0, 1)

    p_sequential += 1
    return p_sequential-1

def remove_object(id:int):
    gp, xy, rot = p_dict[id]

    grid_man.editObject(gp, (xy[0],xy[1]), rot, 0)
    p_dict.pop(id)

def move_object(id:int, new_y, new_x):
    gp, xy, rot = p_dict[id]
    tmp = (gp, (new_x,new_y), rot)
    sentinel = False

    if (right_square(*tmp) < 24 and lowest_square(*tmp) < 10) and left_square(*tmp) > -1:
        sentinel = True
        grid_man.editObject(gp, xy, rot, 0)
        if not grid_man.testSpace(*tmp):
            grid_man.editObject(gp, xy, rot, 1)
            sentinel = False


    if sentinel:
        grid_man.editObject(gp, (new_x, new_y), rot, 1)
        p_dict[id] = (gp, (new_x,new_y), rot)

    return sentinel

def rot_object(id:int, new_rot:int):
    if new_rot > 3: new_rot = new_rot%4

    gp, xy, rot = p_dict[id]

    grid_man.editObject(gp, (xy[0],xy[1]), rot, 0)
    if grid_man.testSpace(*p_dict[id]):
        try:
            grid_man.editObject(gp, (xy[0],xy[1]), new_rot, 1)
            p_dict[id] = (gp, xy, new_rot)
        except IndexError: # leaves debris from squares before error
            grid_man.editObject(gp, (xy[0],xy[1]), rot, 1)
    else:
        grid_man.editObject(gp, (xy[0],xy[1]), rot, 1)


objects = list(GridPiece.__dict__['_member_names_'])

# pieces = list(GridPiece.__dict__.values())[4]
# for i in range(len(pieces)):
#     create_object(GridPiece(pieces[i]), (3*i, 0))

speed = 1
move_lock = time() + 2
speed_lock = 0
move_speed = 0.1

active_piece = create_object(GridPiece(objects[randint(0, len(objects)-1)]), (1, 0))
move_side = 0  # 1 left, 0 none, 2 right

print(grid_man.__str__())

while running:
    # INPUT HANDLING -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_side = 1
            elif event.key == pygame.K_RIGHT:
                move_side = 2
            elif event.key == pygame.K_UP and active_piece != -1:
                rot_object(active_piece, p_dict[active_piece][2]+1)
            elif event.key == pygame.K_DOWN:
                speed = 3
                move_lock = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_side = 0
            elif event.key == pygame.K_RIGHT:
                move_side = 0
            elif event.key == pygame.K_DOWN:
                speed = 1

    if move_side and time()>speed_lock and active_piece != -1:
        if move_side == 1:
            move_object(active_piece, p_dict[active_piece][1][1], p_dict[active_piece][1][0]-1)
        else:
            move_object(active_piece, p_dict[active_piece][1][1], p_dict[active_piece][1][0]+1)
        speed_lock = time()+move_speed
    # ---------------------

    # PHYSICS HANDLING ----
    if time() > move_lock and active_piece != -1:
        b = move_object(active_piece, p_dict[active_piece][1][1]+1, p_dict[active_piece][1][0])
        if not b:
            active_piece = create_object(GridPiece(objects[randint(0, len(objects)-1)]), (1, 0))
            # active_piece = -1
        move_lock = time()+(1/speed)
    # ---------------------

    # DRAWING HANDLING ----
    screen.fill((75, 70, 94))
    for y in range(len(grid_man.t_squares)):
        for x in range(len(grid_man.t_squares[y])):
            pygame.draw.rect(screen, color_dict.get(grid_man.t_squares[y][x]),
                             pygame.Rect(columns.get(x), rows.get(y), 45, 45), border_radius=2)
    pygame.display.flip()
    # ---------------------

pygame.quit()