from definitions import *
from json import loads, dumps
from time import sleep
from initial import init_window

import pygame
from pygame import Rect

screen = init_window(pygame, tuple(map(int, read_pipe().split(", "))))

running = True
while running:
    buffer = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        buffer.append(dumps(event_t(event.type, event.dict).__dict__))
    write_pipe(str(buffer).replace('\'', ""))

    screen.fill((255, 255, 255))

    data = drawable_f(loads(read_pipe()))

    pygame.draw.rect(screen, data.color, Rect(*data.xy, *data.size))

    pygame.display.flip()

pygame.quit()
close()
