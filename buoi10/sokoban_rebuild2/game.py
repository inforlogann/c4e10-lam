import  pygame

class Game:
    def __init__(self):
        pass
    def console_draw(self):
#         draw in console
        for y in range(self.map.height):
            for x in range(self.map.width):
                if y == self.dest.y and x== self.dest.x:
                    print(" D ", end="")
                elif y == self.box.y and x== self.box.x:
                    print(" B ",end ="")
                elif y== self.pusher.y and x== self.pusher.x:
                    print(" P ", end ="")
                else:
                    print(" - ", end = "")
            print()
    def draw_image_center(self,object,screen):
        pixel = 64
        w = (pixel-object.image.get_width())/2 +object.x *pixel
        h = (pixel- object.image.get_height())/2 +object.y *pixel
        screen.blit(object.image,(w,h))
    def in_map(self,object,dx,dy):
        if  0<= object.x+dx< self.map.width and 0<=object.y+dy < self.map.height:
            return True
        else:
            return False

    def draw(self,screen,ground_image):
        pixel = 64
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
    def  handle_input(self,event):
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
        if self.pusher.collide(self.box,dx,dy):
            if self.in_map(self.box,dx,dy):
                self.box.move(dx,dy)
                self.pusher.move(dx,dy)
        elif self.in_map(self.pusher,dx,dy):
            self.pusher.move(dx,dy)

    def check_win(self):
        if self.box.x == self.dest.x and self.box.y == self.dest.y:
            return True
        else:
            return False