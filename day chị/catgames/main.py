from gamecontrollers.gamecontrollers import GameController
from gameviews.gameviews import GameView
from gameviews.catview import CatView
from gamemodels.gamemodels import GameModel

import  random

import pygame
pygame.init()
screen = pygame.display.set_mode((1300, 950))
done = False


catmodel = GameModel(325, 500)
catmodel.move(50, 50)

groundmodel = GameModel(10, 40)


bonemodel = GameModel((random.randrange(300,900)),50)

boneview = GameView(pygame.image.load("images/bone.png"),screen)
def setbone():
    bonemodel.x= 400
    bonemodel.y += 50




fishmodel = GameModel((random.randrange(300,900)),50)
fish_list=[
    pygame.image.load("images/fish1.png"),
    pygame.image.load ( "images/fish2.png" ),
    pygame.image.load ( "images/fish3.png" ),
    pygame.image.load ( "images/fish4.png" )
]

fishview = GameView(random.choice(fish_list),screen)
def setfish():
    fishmodel.x = 500
    fishmodel.y +=50


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
    setfish()
    setbone()
    bone.draw ()
    fish.draw()
    cat.draw ()
    pygame.display.flip()

