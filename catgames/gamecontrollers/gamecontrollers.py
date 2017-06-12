import  pygame
from gameviews.gameviews import  GameView


class GameController:
    def __init__(self,gamemodel,gameview):
        self.gamemodel = gamemodel
        self.gameview = gameview
        self.counter = 0

    def draw(self):
        self.gameview.draw ( self.gamemodel )

    def move(self, dx, dy):
        self.gamemodel.move ( dx, dy )

    def handle_input(self, event):
        dx = 0
        dy = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print ( 11 )
                dy -= 1
            elif event.key == pygame.K_DOWN:
                dy += 1
            elif event.key == pygame.K_RIGHT:
                dx += 1
            elif event.key == pygame.K_LEFT:
                dx -= 1
            elif event.key == pygame.K_ESCAPE:
                quit ()
        print ( dx, dy )
        self.move ( dx * 10, dy * 10 )
        print ( self.gamemodel.x, self.gamemodel.y )