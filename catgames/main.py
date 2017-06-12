from gamecontrollers.gamecontrollers import GameController
from gameviews.gameviews import GameView
from gameviews.catview import CatView
from gamemodels.gamemodels import GameModel
from random import  randint
import  os,random

import pygame
pygame.init()
screen = pygame.display.set_mode((1300, 950))
done = False


catmodel = GameModel(325, 500)
catmodel.move(50, 50)

groundmodel = GameModel(10, 40)

bonemodel = GameModel((randint(300,900)),50)
boneview = GameView(pygame.image.load("images/bone.png"),screen)

fishmodel = GameModel((randint(300,900)),20)
fish_list=[
    pygame.image.load("images/babelfish.png"),
    pygame.image.load ( "images/fish.png" ),
    pygame.image.load ( "images/gnomefish.png" ),
    pygame.image.load ( "images/bluefish.png" )
]

fishview = GameView(random.choice(fish_list),screen)

cat_animations = [
    pygame.image.load("images/cat_right.png"),
    pygame.image.load("images/cat_left.png")
                    ]
catview = CatView(cat_animations, screen)
groundview = GameView(pygame.image.load("images/ground.png"), screen)



fish = GameController(fishmodel,fishview)
bone = GameController(bonemodel,boneview)
cat = GameController(catmodel, catview)
ground = GameController(groundmodel, groundview)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        cat.handle_input(event)
    ground.draw()


    bone.draw ()
    fish.draw()
    cat.draw ()
    pygame.display.flip()

