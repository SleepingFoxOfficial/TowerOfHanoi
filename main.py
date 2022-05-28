import pygame
import mylib as lib


totalN = 5
mtx = lib.countDisks(totalN, 1, 2, 3)

pygame.init()
win = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Towers of Hanoi")

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    lib.visualTower(totalN, mtx, win, 100)
    pygame.display.update()
pygame.quit()
