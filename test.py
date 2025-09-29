import pygame
import sys

pygame.init()

breite = 600
höhe = 600

screen = pygame.display.set_mode((breite, höhe))
pygame.display.set_caption("Game")

sprite_sheet_image = pygame.image.load("play.png").convert_alpha()

HG = (0, 0, 0)

move_left = False
move_right = False
move_up = False
move_down = False

while run == True:
    screen.fill(HG)
    screen.blit(sprite_sheet_image, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RIGHT):
                move_right = True
            if (event.key == pygame.K_LEFT):
                move_left = True
            if (event.key == pygame.K_UP):
                move_up = True
            if (event.key == pygame.K_DOWN):
                move_down = True
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RIGHT):
                move_right = True
            if (event.key == pygame.K_LEFT):
                move_left = True
            if (event.key == pygame.K_UP):
                move_up = True
            if (event.key == pygame.K_DOWN):
                move_down = True
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()

pygame.quit
