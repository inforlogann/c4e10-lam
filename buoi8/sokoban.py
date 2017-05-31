import pygame

class Game:
    def __init__(self):
        pass
    def console_draw(self):
#         draw in console
        for y in range(self.map.height):
            for x in range(self.map.width):
                if y == self.dest.y and x== self.dest.x:
                    print("D", end="")
                elif y == self.box.y and x== self.box.x:
                    print("B",end ="")
                elif y== self.pusher.y and x== self.pusher.x:
                    print("P", end ="")
                else:
                    print(" - ", end = "")
            print()
    def draw_image_center(self,object,screen):
        w = (pixel-object.image.get_width())/2 +object.x *pixel
        h = (pixel- object.image.get_height())/2 +object.y *pixel
        screen.blit(object.image,(w,h))

    def draw(self):
#         draw in pygame
        for i in range(self.map.width):
            for j in range(self.map.height):
                screen.blit(ground_image,(i * pixel, j * pixel))
        # screen.blit(pusher_image,(self.pusher.x*pixel,self.pusher.y*pixel))
        # screen.blit(box_image,(self.box.x*pixel,self.box.y*pixel))
        # screen.blit(dest_image,(self.dest.x*pixel,self.dest.y*pixel))
        self.draw_image_center(self.pusher,screen)
        self.draw_image_center(self.box,screen)
        self.draw_image_center(self.dest,screen)

        pass

class Map:
    def __init__(self,w,h):
        self.width=w
        self.height=h
class Pusher:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        dx = 0
        dy = 0


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            if event.key == pygame.K_RIGHT:
                dx = 1
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = 1
        return  dx, dy
class Box:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Dest:
    def __init__(self,x,y):
        self.x = x
        self.y = y

sokoban = Game()
sokoban.map=Map(10,10)
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
        dx,dy = sokoban.pusher.move()
    sokoban.pusher.x +=dx
    sokoban.pusher.y +=dy


    sokoban.draw()

    pygame.display.flip()