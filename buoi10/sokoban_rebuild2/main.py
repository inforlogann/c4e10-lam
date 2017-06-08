import pygame

from game import Game
from game_object.box import Box
from game_object.dest import Dest
from game_object.map import Map
from game_object.pusher import Pusher

sokoban = Game()
sokoban.map=Map(6,6)
sokoban.pusher = Pusher(1,1)
sokoban.box = Box(2,2)
sokoban.dest = Dest(3,3)
sokoban.console_draw()



pygame.init()
screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("Sokoban")
done = False
box_image = pygame.image.load("images/box.png")
pusher_image = pygame.image.load("images/pusher.png")
ground_image = pygame.image.load("images/ground.png")
dest_image = pygame.image.load("images/dest.png")
wall_image = pygame.image.load("images/wall.png")
sokoban.box.image= box_image
sokoban.dest.image = dest_image
sokoban.pusher.image =  pusher_image
pixel = 64

while not done:
    dx=0
    dy=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        sokoban.handle_input(event)



    sokoban.draw(screen,ground_image)
    if sokoban.check_win():
        sokoban.box.image = pygame.image.load("images/box_victory.png")
        sokoban.draw(screen,ground_image)
        done = True
    pygame.display.flip()