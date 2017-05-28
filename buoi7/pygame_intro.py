import pygame


pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Sokoban")
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dy -=1
            if event.type == pygame.K_RIGHT:
                dx +=1
            if event.type == pygame.K_UP:
                dy +=1
            if event.type == pygame.K_DOWN:
                dy -=1

    pygame.display.flip()

