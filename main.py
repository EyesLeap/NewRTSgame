import pygame
import sys
from Entity import Entity
from components import Damage, Health
from uuid import uuid4
from collections import OrderedDict as dict
clock = pygame.time.Clock()
fps = 30
WHITE = (255,255,255)
GREEN = (34,139,34)
class A:
    def __init__(self):
        self.x = 5



def run():
    player = Entity('player')
    player.health = Health()
    print(str(player.health))

    pygame.init()
    screen = pygame.display.set_mode((1280,800))
    pygame.display.set_caption("Залупа")
    pygame.draw.rect(screen, WHITE, (10,10,1260, 780), 2)
    pygame.draw.rect(screen, WHITE, (1034,10,270, 780), 2)
    pygame.draw.rect(screen, GREEN, (12,12,32, 32))
    pygame.draw.rect(screen, GREEN, (532,532,32, 32))
    pygame.draw.rect(screen, GREEN, (564,564,32, 32))
    pygame.display.update()
    bg_color = (0,0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)


        clock.tick(fps)

run()